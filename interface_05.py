"""
https://qiita.com/nrslib/items/73bf176147192c402049#interface

interfaceをつかって抽象化
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


class Program:
    def process(self, convert_type: str, data: List[str]):
        converter = self.create_converter(convert_type)

        output = converter.convert(data)

        if len(data) > 10:
            message = "Many elements."
        else:
            message = "Few elements."

        print(message)
        print(output)

    def create_converter(self, convert_type: str) -> IConverter:
        if convert_type == "csv":
            return CsvConverter()
        elif convert_type == "tsv":
            return TsvConverter()
        else:
            raise ValueError(f"{convert_type} is invalid.")


if __name__ == "__main__":
    data = ["Bob", "Tom", "Ken"]

    Program().process("csv", data)
    Program().process("tsv", data)
    # Program().process("psv", data) # ValueError: psv is invalid.
