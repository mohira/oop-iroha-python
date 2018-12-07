"""
https://qiita.com/nrslib/items/73bf176147192c402049#interface

別解: メソッドを返す
"""
from typing import List


def join_by_comma(data: List[str]) -> str:
    if data:
        csv = data[0]
    else:
        csv = ""
    for d in data[1:]:
        csv += f",{d}"

    return csv


def join_by_tab(data: List[str]) -> str:
    if data:
        tsv = data[0]
    else:
        tsv = ""
    for d in data[1:]:
        tsv += f"\t{d}"

    return tsv


class Program:
    def process(self, convert_type: str, data: List[str]):
        output = self.create_output(convert_type)

        if len(data) > 10:
            message = "Many elements."
        else:
            message = "Few elements."

        print(message)
        print(output)

    def create_output(self, convert_type: str) -> str:
        if convert_type == "csv":
            return join_by_comma(data)
        elif convert_type == "tsv":
            return join_by_tab(data)
        else:
            raise ValueError(f"{convert_type} is invalid.")


if __name__ == "__main__":
    data = ["Bob", "Tom", "Ken"]

    Program().process("csv", data)
    Program().process("tsv", data)
    # Program().process("psv", data) # ValueError: psv is invalid.
