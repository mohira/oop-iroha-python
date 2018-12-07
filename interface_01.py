"""
https://qiita.com/nrslib/items/73bf176147192c402049#interface

議論はここから始める

str.join()などを使えば 条件分岐内部の処理はスッキリ書けるけれど、敢えて記事通りのままにしている
"""

from typing import List


class Program:
    def process(self, convert_type: str, data: List[str]) -> None:
        if convert_type == "csv":
            if data:
                csv = data[0]
            else:
                csv = ""
            for d in data[1:]:
                csv += f",{d}"

            output = csv

        elif convert_type == "tsv":
            if data:
                tsv = data[0]
            else:
                tsv = ""
            for d in data[1:]:
                tsv += f"\t{d}"

            output = tsv

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
