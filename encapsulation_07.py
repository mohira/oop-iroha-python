"""
https://qiita.com/nrslib/items/73bf176147192c402049#6getter-%E3%81%AF%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84
"""
from typing import List


class Logic:
    def __init__(self, source: List[int]):
        self.num_element = len(source)
        self.data = source

    def sum(self) -> int:
        result = 0

        for i in range(self.num_element + 1):
            result += i

        return result


class Member:
    pass


class Team:
    def __init__(self):
        self.members: List[Member] = []

    def join(self, member: Member) -> None:
        if len(member) >= 50:
            raise Exception("最大人数を超過します")

        self.members.append(member)


def add_member(team: Team, member: Member) -> None:
    if len(team.members) >= 50:
        raise Exception("最大人数を超過します")

    team.members.append(member)
