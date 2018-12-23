"""
https://qiita.com/nrslib/items/73bf176147192c402049#1%E5%88%9D%E6%9C%9F%E5%8C%96%E3%81%AF%E3%82%B3%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF
"""
from logging import Logger


class BusinessLogic:
    def __init__(self, is_product: bool, logger: Logger):
        self.is_product = is_product
        self.logger = logger

    def execute(self) -> None:
        pass
