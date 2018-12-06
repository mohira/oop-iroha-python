"""
https://qiita.com/nrslib/items/73bf176147192c402049#class

関数による抽象化
"""

from typing import List


def write(write_type: str, data: List[str]) -> None:
    if write_type == "console":
        write_console(data)
    elif write_type == "file":
        write_file(data)
    else:
        raise ValueError(f"write_type: {write_type} is invalid argument.")


def write_console(data: List[str]) -> None:
    print("Data: ")
    for element in data:
        print(f"- {element}")


def write_file(data: List[str]) -> None:
    text = ",".join(data)
    with open("output.txt", "w") as f:
        print(text, file=f)


if __name__ == "__main__":
    data = ["Bob", "Tom", "Ken"]

    write("console", data)

    write("file", data)

    # write("CONSOLE", data) # ValueError
