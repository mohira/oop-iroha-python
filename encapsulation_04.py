"""
https://qiita.com/nrslib/items/73bf176147192c402049#3%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89%E3%81%AB%E5%89%8D%E5%BE%8C%E9%96%A2%E4%BF%82%E3%81%AF%E4%BD%9C%E3%82%89%E3%81%AA%E3%81%84
"""
import datetime


class Logger:
    def log(self, param):
        pass


class BusinessLogic:
    def execute(self) -> None:
        self.before_execute()

        self.logger.log(f"Execute on {datetime.datetime.now()}")

    def before_execute(self):
        self.logger = Logger()
