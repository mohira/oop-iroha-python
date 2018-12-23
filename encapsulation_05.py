"""
https://qiita.com/nrslib/items/73bf176147192c402049#4%E5%89%AF%E4%BD%9C%E7%94%A8%E3%82%92%E3%82%8F%E3%81%8B%E3%82%8A%E3%82%84%E3%81%99%E3%81%8F
"""


class Command:
    def __init__(self, id_: int, operation: str):
        self.id = id_
        self.operation = operation


class CommandHandlerBefore:
    def validate(self, command: Command) -> bool:
        if command.operation == "nop":
            command.operation = None

        if command.id < 0:
            return False

        return True

    def handle(self, command: Command) -> None:
        if command.operation is None:
            return
        else:
            if command.operation == "add":
                pass  # 追加処理
            elif command.operation == "update":
                pass  # 更新処理
            elif command.operation == "del":
                pass  # 削除処理


class CommandHandler:
    def validate(self, command: Command) -> bool:
        if command.id < 0:
            return False

        return True

    def handle(self, command: Command) -> None:
        if command.operation == "nop" or command.operation is None:
            return
        else:
            if command.operation == "add":
                pass  # 追加処理
            elif command.operation == "update":
                pass  # 更新処理
            elif command.operation == "del":
                pass  # 削除処理


if __name__ == "__main__":
    command = Command(-1, "nop")
    # handler = CommandHandlerBefore()
    handler = CommandHandler()

    if handler.validate(command):
        handler.handle(command)
    else:
        print(command.operation)
