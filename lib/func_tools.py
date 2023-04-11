"""Function tools"""
import sys
from logging import Logger


def function_will_exit_failure(error_message: str, logger: Logger) -> None:
    """System exit with message for failure"""
    try:
        if logger:
            logger.error(error_message)
        sys.exit(error_message or 1)
    except SystemExit as e:
        # this log will include traceback
        logger.exception("function_will_exit_failure failed with exception")
        # this log will just include content in sys.exit
        logger.error(str(e))
        raise
