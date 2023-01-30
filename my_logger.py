import datetime
import logging
from logging.handlers import RotatingFileHandler

loggers = {}


# cải tiến logger thành CSV format


def myLogger(name):
    # global loggers

    if loggers.get(name):
        return loggers.get(name)
    else:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        now = datetime.datetime.now()
        handler = logging.FileHandler(
            "/root/credentials/Logs/ProvisioningPython"
            + now.strftime("%Y-%m-%d")
            + ".log"
        )
        formatter = logging.Formatter("[%(asctime)s] - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        loggers.update(dict(name=logger))

        return logger


def setup_logger(logger_name, log_file, level=logging.DEBUG):
    # global loggers
    if loggers.get(logger_name):
        # print('logger exits', logger_name)
        return loggers.get(logger_name)
    else:
        # print('logger not exits', logger_name)
        formatter = logging.Formatter("[%(asctime)s] - %(levelname)s - %(message)s")
        # fileHandler = logging.FileHandler(log_file)
        # fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        streamHandler.setLevel(level)

        my_handler = RotatingFileHandler(
            log_file,
            mode="a",
            maxBytes=7 * 1024 * 1024,
            backupCount=10,
            encoding="utf8",
            delay=0,
        )
        # my_handler = RotatingFileHandler(log_file, mode='a', maxBytes=512, backupCount=10, encoding=None,
        #                                  delay=0)
        my_handler.setFormatter(formatter)
        my_handler.setLevel(level)

        app_log = logging.getLogger(logger_name)
        app_log.setLevel(level)
        app_log.addHandler(streamHandler)
        app_log.addHandler(my_handler)

        loggers.update({logger_name: app_log})
        return app_log


class Logger:
    def __init__(self, logger_name, log_file):
        self.__log = setup_logger(logger_name, log_file)
        # return self.__log

    def error(self, msg):
        self.__log.error(msg)

    def debug(self, msg):
        self.__log.debug(msg)

    def warning(self, msg):
        self.__log.warning(msg)

    def info(self, msg):
        # print(utils.unicodeToUnsign(msg))
        self.__log.info(msg)

    def critical(self, msg):
        self.__log.critical(msg)

class LogHandler:
    def error(self, msg):
        self.__log.error(msg)

    def debug(self, msg):
        self.__log.debug(msg)

    def warning(self, msg):
        self.__log.warning(msg)

    def info(self, msg):
        self.__log.info(msg)

    def critical(self, msg):
        self.__log.critical(msg)