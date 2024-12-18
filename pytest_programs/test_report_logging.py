import logging

"""
def test_logging_demo():

    filehandler = logging.FileHandler("LogFile.log")
    format_msg = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s, %(message)s")
    filehandler.setFormatter(format_msg)

    logger = logging.getLogger(__name__)
    logger.addHandler(filehandler)

    logger.setLevel(logging.INFO)  # set level which it will print, here it will print from info to critical
    logger.debug("A debug statement is executed")
    logger.info("Information of Test Result")
    logger.warning("Warning")
    logger.error("Error")
    logger.critical("Critical Error")


def test_logging_format_demo():
    file_handler1 = logging.FileHandler("new_logfile.log")
    log_format = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file_handler1.setFormatter(log_format)

    logger1 = logging.getLogger(__name__)
    logger1.addHandler(file_handler1)

    logger1.setLevel(logging.INFO)
    logger1.debug("Its a debug message")
    logger1.info("This is info")
    logger1.warning("This is warning")
    logger1.error(" This is error")
    logger1.critical("This is very critical")


"""


def test_logging_setup():
    filehandler2 = logging.FileHandler("practice_logfile.log")
    logging_format = logging.Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s")
    filehandler2.setFormatter(logging_format)

    logger2 = logging.getLogger(__name__)
    logger2.addHandler(filehandler2)

    logger2.setLevel(logging.DEBUG)

    logger2.info("This is INFO")
    logger2.debug("This is DEBUG")
    logger2.error("This is ERROR")
    logger2.warning("This is WARNING")
    logger2.critical("This is CRITICAL")

