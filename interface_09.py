"""
https://qiita.com/nrslib/items/73bf176147192c402049#interface

convert内をスッキリさせた
"""
from abc import ABCMeta, abstractmethod
from typing import List


class IConverter(metaclass=ABCMeta):
    @abstractmethod
    def convert(self, data: List[str]) -> str:
        pass


class CsvConverter(IConverter):
    def convert(self, data: List[str]) -> str:
        return ",".join(data)


class TsvConverter(IConverter):
    def convert(self, data: List[str]) -> str:
        return "\t".join(data)


class PipeJoinConverter(IConverter):
    def convert(self, data: List[str]) -> str:
        return "|".join(data)


class IEvaluator(metaclass=ABCMeta):
    @abstractmethod
    def evaluate(self, data: List[str]) -> None:
        pass


class NormalEvaluator(IEvaluator):
    def evaluate(self, data: List[str]) -> None:
        if len(data) > 10:
            print("Many elements.")
        else:
            print("Few elements.")


class IsEvenEvaluator(IEvaluator):
    def evaluate(self, data: List[str]) -> None:
        if len(data) % 2 == 0:
            print("even")
        else:
            print("odd")


class Program:
    def process(self, converter: IConverter, data: List[str], evaluator: IEvaluator):
        output = converter.convert(data)

        evaluator.evaluate(data)
        print(output)


if __name__ == "__main__":
    data = ["Bob", "Tom", "Ken"]

    Program().process(CsvConverter(), data, NormalEvaluator())
    Program().process(TsvConverter(), data, NormalEvaluator())
    Program().process(PipeJoinConverter(), data, NormalEvaluator())

    Program().process(CsvConverter(), data, IsEvenEvaluator())
    Program().process(TsvConverter(), data, IsEvenEvaluator())
    Program().process(PipeJoinConverter(), data, IsEvenEvaluator())
