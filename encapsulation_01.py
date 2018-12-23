"""
https://qiita.com/nrslib/items/73bf176147192c402049#%E3%82%AB%E3%83%97%E3%82%BB%E3%83%AB%E5%8C%96%E3%81%8C%E3%81%AA%E3%81%9C%E5%BF%85%E8%A6%81%E3%81%AA%E3%81%AE%E3%81%8B

"""


class BusinessLogic:
    def process(self):
        pass

    def set_logger(self, logger: Logger):
        pass


if __name__ == "__main__":
    logic = BusinessLogic()

    # logic.process() # NameError: name 'Logger' is not defined
