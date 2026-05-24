import logging
import os
from datetime import datetime

# Created ONCE when logger.py is first imported — same for entire run
_log_filename = datetime.now().strftime("test_run_%Y%m%d_%H%M%S.log")
_log_filepath = os.path.join("logs", _log_filename)


def get_logger(name):

    # Create logs folder if it does not exist
    os.makedirs("logs", exist_ok=True)

    # Create logger with given name
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers if logger already exists
    if logger.handlers:
        return logger

    # Console handler — prints logs to terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)  # ✅ FIXED

    # File handler — saves logs to same file for entire run
    file_handler = logging.FileHandler(_log_filepath, encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger