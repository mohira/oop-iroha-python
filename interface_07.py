"""
https://qiita.com/nrslib/items/73bf176147192c402049#interface

interfaceをならではの記述 そして Pipe区切り
"""
from abc import ABCMeta, abstractmethod
from typing import List


class IConverter(metaclass=ABCMeta):
    @abstractmethod
    def convert(self, data: List[str]) -> str:
        pass


class CsvConverter(IConverter):
    def convert(self, data: List[str]) -> str:
        if data:
            csv = data[0]
        else:
            csv = ""
        for d in data[1:]:
            csv += f",{d}"

        return csv


class TsvConverter(IConverter):
    def convert(self, data: List[str]) -> str:
        if data:
            tsv = data[0]
        else:
            tsv = ""
        for d in data[1:]:
            tsv += f"\t{d}"

        return tsv


class PipeJoinConverter(IConverter):
    def convert(self, data: List[str]) -> str:
        if data:
            text = data[0]
        else:
            text = ""

        for d in data[1:]:
            text += f"|{d}"

        return text


class Program:
    def process(self, converter: IConverter, data: List[str]):
        output = converter.convert(data)

        if len(data) > 10:
            message = "Many elements."
        else:
            message = "Few elements."

        print(message)
        print(output)


if __name__ == "__main__":
    data = ["Bob", "Tom", "Ken"]

    Program().process(CsvConverter(), data)
    Program().process(TsvConverter(), data)
    Program().process(PipeJoinConverter(), data)
