import logging.handlers


class classLogger(object):
    """
    Класс который хранит данные приложения

    """

    def __init__(self):
        """Constructor"""
        self.logger = None
        self.logerCreate()

    def logerCreate(self):
        # logging.basicConfig(level=logging.DEBUG)
        rfh = logging.handlers.RotatingFileHandler(
            filename='zip_app.log',
            mode='a',
            maxBytes=5 * 1024 * 1024,
            backupCount=9,
            encoding=None,
            delay=0
        )
        logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO, datefmt="%y-%m-%d %H:%M:%S",
                            handlers=[rfh])
        self.logger = logging.getLogger('main')

    def getLogger(self):
        return self.logger

    def info(self, str):
        self.logger.info(str)


myLogger: classLogger = classLogger()
