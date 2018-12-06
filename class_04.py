"""
https://qiita.com/nrslib/items/73bf176147192c402049#class

クラスへの書き換え
"""

from typing import List


class Writer:
    def __init__(self):
        self.write_type: str = ""
        self.data: List[str] = []

    def write(self) -> None:
        if self.write_type == "console":
            self.write_console(self.data)
        elif self.write_type == "file":
            self.write_file(self.data)
        else:
            raise ValueError(f"write_type: {self.write_type} is invalid argument.")

    def write_console(self, data: List[str]) -> None:
        print("Data: ")
        for element in data:
            print(f"- {element}")

    def write_file(self, data: List[str]) -> None:
        text = ",".join(data)
        with open("output.txt", "w") as f:
            print(text, file=f)


if __name__ == "__main__":
    writer = Writer()
    writer.write_type = "console"
    writer.data = ["Bob", "Tom", "Ken"]

    writer.write()
