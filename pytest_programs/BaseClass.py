import inspect
import logging

"""
class BaseClass:
    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        filehandler = logging.FileHandler("LogFile.log")
        format_msg = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s, %(message)s")
        filehandler.setFormatter(format_msg)
        logger = logging.getLogger(loggerName)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        return logger
"""


class BaseClass:
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        filehandler = logging.FileHandler("New_LogFile.log")
        format_file = logging.Formatter("%(asctime)s, %(name)s, %(levelname)s, %(message)s")
        filehandler.setFormatter(format_file)

        logger = logging.getLogger(logger_name)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
