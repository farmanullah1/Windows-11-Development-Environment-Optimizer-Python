"""Logging utilities with path anonymization and secret redaction."""

import os
import re
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional

# Patterns to redact from logs
SENSITIVE_PATTERNS = [
    re.compile(r'(token[=:\s"]+)([a-zA-Z0-9_\-\.]{8,})', re.IGNORECASE),
    re.compile(r'(password[=:\s"]+)([^\s",]{4,})', re.IGNORECASE),
    re.compile(r'(secret[=:\s"]+)([a-zA-Z0-9_\-\.]{8,})', re.IGNORECASE),
    re.compile(r'(key[=:\s"]+)([a-zA-Z0-9_\-\.]{16,})', re.IGNORECASE),
    re.compile(r'(bearer\s+)([a-zA-Z0-9_\-\.]{16,})', re.IGNORECASE),
]


class RedactingFormatter(logging.Formatter):
    """Custom logging formatter that strips sensitive credentials and anonymizes usernames."""

    def __init__(self, fmt: Optional[str] = None, datefmt: Optional[str] = None):
        super().__init__(fmt, datefmt)
        self.userprofile = os.environ.get("USERPROFILE", "")
        self.username = os.environ.get("USERNAME", "")

    def format(self, record: logging.LogRecord) -> str:
        msg = super().format(record)
        # Anonymize username / userprofile path
        if self.userprofile and self.userprofile in msg:
            msg = msg.replace(self.userprofile, "%USERPROFILE%")
        if self.username and self.username in msg and len(self.username) > 2:
            msg = msg.replace(f"\\{self.username}\\", "\\%USERNAME%\\")

        # Redact known credential patterns
        for pattern in SENSITIVE_PATTERNS:
            msg = pattern.sub(r"\1[REDACTED]", msg)

        return msg


def setup_logger(name: str = "optimizer", log_level: str = "normal") -> logging.Logger:
    """Configures rotating file logger and safe console output."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    level = logging.DEBUG if log_level == "verbose" else logging.INFO
    logger.setLevel(level)

    formatter = RedactingFormatter(
        fmt="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    # Safe log directory under %LOCALAPPDATA%\Win11DevOptimizer\logs
    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        log_dir = Path(local_app_data) / "Win11DevOptimizer" / "logs"
        try:
            log_dir.mkdir(parents=True, exist_ok=True)
            log_file = log_dir / "optimizer.log"
            file_handler = RotatingFileHandler(
                log_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
            )
            file_handler.setFormatter(formatter)
            file_handler.setLevel(level)
            logger.addHandler(file_handler)
        except OSError:
            # Fail closed gracefully if directory cannot be created
            pass

    return logger
