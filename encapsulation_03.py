"""
https://qiita.com/nrslib/items/73bf176147192c402049#2%E8%87%AA%E7%94%B1%E3%81%AA%E5%9E%8B%E3%82%92%E4%BE%BF%E5%88%A9%E3%81%AB%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84
"""
from enum import Enum, auto


class Mode(Enum):
    product = auto()
    test = auto()


class BusinessLogic:
    def __init__(self, mode: Mode):
        self.mode = mode

    def execute(self) -> None:
        pass
