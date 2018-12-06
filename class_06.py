"""
https://qiita.com/nrslib/items/73bf176147192c402049#class

"console" や "file" などの文字列を利用しない
"""

from typing import List


class ConsoleWriter:
    def __init__(self, data: List[str]):
        self.data = data

    def write(self) -> None:
        print("Data: ")
        for element in self.data:
            print(f"- {element}")


class FileWriter:
    def __init__(self, data: List[str]):
        self.data = data

    def write(self) -> None:
        text = ",".join(self.data)
        with open("output.txt", "w") as f:
            print(text, file=f)


if __name__ == "__main__":
    writer = ConsoleWriter(["Bob", "Tom", "Ken"])

    writer.write()
