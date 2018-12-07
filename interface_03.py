"""
https://qiita.com/nrslib/items/73bf176147192c402049#interface

今度は クラス で 抽象化
"""

from typing import List


class CsvConverter:
    def convert(self, data: List[str]) -> str:
        if data:
            csv = data[0]
        else:
            csv = ""
        for d in data[1:]:
            csv += f",{d}"

        return csv


class TsvConverter:
    def convert(self, data: List[str]) -> str:
        if data:
            tsv = data[0]
        else:
            tsv = ""
        for d in data[1:]:
            tsv += f"\t{d}"

        return tsv


class Program:
    def process(self, convert_type: str, data: List[str]) -> None:
        if convert_type == "csv":
            converter = CsvConverter()
            output = converter.convert(data)
        elif convert_type == "tsv":
            converter = TsvConverter()
            output = converter.convert(data)
        else:
            raise ValueError(f"{convert_type} is invalid.")

        if len(data) > 10:
            message = "Many elements."
        else:
            message = "Few elements."

        print(message)
        print(output)


if __name__ == "__main__":
    data = ["Bob", "Tom", "Ken"]

    Program().process("csv", data)
    Program().process("tsv", data)
    # Program().process("psv", data) # ValueError: psv is invalid.
