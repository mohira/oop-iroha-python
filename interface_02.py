"""
https://qiita.com/nrslib/items/73bf176147192c402049#interface

条件分岐を減らすためにメソッドを使って抽象化
処理は見やすくなったけれど、条件分岐は残ったまま...

"""

from typing import List


class Program:
    def process(self, convert_type: str, data: List[str]) -> None:
        if convert_type == "csv":
            output = self.join_by_comma(data)

        elif convert_type == "tsv":
            output = self.join_by_tab(data)

        else:
            raise ValueError(f"{convert_type} is invalid.")

        if len(data) > 10:
            message = "Many elements."
        else:
            message = "Few elements."

        print(message)
        print(output)

    def join_by_comma(self, data: List[str]) -> str:
        if data:
            csv = data[0]
        else:
            csv = ""
        for d in data[1:]:
            csv += f",{d}"

        return csv

    def join_by_tab(self, data: List[str]) -> str:
        if data:
            tsv = data[0]
        else:
            tsv = ""
        for d in data[1:]:
            tsv += f"\t{d}"

        return tsv


if __name__ == "__main__":
    data = ["Bob", "Tom", "Ken"]

    Program().process("csv", data)
    Program().process("tsv", data)
    # Program().process("psv", data) # ValueError: psv is invalid.
