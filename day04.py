from typing import NamedTuple

class Card(NamedTuple):
    win: set[int]
    nos: set[int]

def open_txt(filename: str) -> list[Card]:
    with open(filename) as f:
        lines = []
        for line in f:
            colon = line.find(":")
            pipe = line.find("|")
            win = set(int(x) for x in line[colon + 1 : pipe].split())
            nos = set(int(x) for x in line[pipe + 1 :].split())
            lines.append(Card(win, nos))
    return lines

def total_pts(cards: list[Card]) -> int:
    result = 0
    for card in cards:
        won = len(card.win.intersection(card.nos))
        if won: result += 2 ** (won - 1)
    return result

if __name__ == "__main__":
    # cards = open_txt("test.txt")
    cards = open_txt("day04.txt")
    print("Part 1: ", total_pts(cards))
