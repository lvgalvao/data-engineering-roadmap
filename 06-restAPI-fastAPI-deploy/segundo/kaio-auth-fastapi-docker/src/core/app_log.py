import logging
import os

from fastapi.logger import logger as fastapi_logger

if "gunicorn" in os.environ.get("SERVER_SOFTWARE", ""):
    """
    When running with gunicorn the log handlers get suppressed instead of
    passed along to the container manager. This forces the gunicorn handlers
    to be used throughout the project.
    """

    gunicorn_logger = logging.getLogger("gunicorn")
    log_level = gunicorn_logger.level

    root_logger = logging.getLogger()
    gunicorn_error_logger = logging.getLogger("gunicorn.error")
    uvicorn_access_logger = logging.getLogger("uvicorn.access")

    # Use gunicorn error handlers for root, uvicorn, and fastapi loggers
    root_logger.handlers = gunicorn_error_logger.handlers
    uvicorn_access_logger.handlers = gunicorn_error_logger.handlers
    fastapi_logger.handlers = gunicorn_error_logger.handlers

    # Pass on logging levels for root, uvicorn, and fastapi loggers
    root_logger.setLevel(log_level)
    uvicorn_access_logger.setLevel(log_level)
    fastapi_logger.setLevel(log_level)
