from loguru import logger


class Logger:

    @staticmethod
    def get_logger():
        logger.add('log_test.log', level='DEBUG', format='{time} - {level} - {message}')


