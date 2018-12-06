"""
https://qiita.com/nrslib/items/73bf176147192c402049#class

ここが出発点
"""

from typing import List


def write(write_type: str, data: List[str]) -> None:
    if write_type == "console":
        print("Data: ")
        for element in data:
            print(f"- {element}")

    elif write_type == "file":
        text = ",".join(data)
        with open("output.txt", "w") as f:
            print(text, file=f)

    else:
        raise ValueError(f"write_type: {write_type} is invalid argument.")


if __name__ == "__main__":
    data = ["Bob", "Tom", "Ken"]

    write("console", data)

    write("file", data)

    # write("CONSOLE", data) # ValueError
