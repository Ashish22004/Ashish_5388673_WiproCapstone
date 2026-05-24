import logging
import os
from datetime import datetime


def get_logger(name):

    # Create logger with given name
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers if logger already exists
    if logger.handlers:
        return logger

    # Ensure logs folder exists when get_logger is first called
    # (NOT at module import time — avoids issue when bat deletes logs folder)
    os.makedirs("logs", exist_ok=True)

    # Use one shared log filename per process (stored on root logger)
    root = logging.getLogger("_wipro_run_")
    if not hasattr(root, "_log_filepath"):
        _log_filename = datetime.now().strftime("test_run_%Y%m%d_%H%M%S.log")
        root._log_filepath = os.path.join("logs", _log_filename)

    _log_filepath = root._log_filepath

    # Console handler — only WARNING and above shown in terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)

    # File handler — saves all INFO+ to one log file for entire run
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