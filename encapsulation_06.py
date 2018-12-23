"""
https://qiita.com/nrslib/items/73bf176147192c402049#5setter-%E3%81%AF%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84
"""


class Logger:
    def log(self, msg) -> None:
        pass


class BusinessLogic:
    def execute(self, logger: Logger = None) -> None:
        if logger is not None:
            logger.log("Starting")
