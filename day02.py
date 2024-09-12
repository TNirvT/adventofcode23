import re
from collections import namedtuple

Cubes = namedtuple("Cubes", ["red", "green", "blue"])

def read_game(line: str) -> list[Cubes]:
    game = []
    for draw in line.split(";"):
        red = re.search(r"\d+(?=red)", draw.replace(" ", ""))
        green = re.search(r"\d+(?=green)", draw.replace(" ", ""))
        blue = re.search(r"\d+(?=blue)", draw.replace(" ", ""))
        game.append(Cubes(
            int(red.group(0)) if red else 0,
            int(green.group(0)) if green else 0,
            int(blue.group(0)) if blue else 0
        ))
    return game

def open_txt(filename: str) -> list[list[Cubes]]:
    with open(filename) as f:
        lines = []
        for line in f:
            colon_idx = line.find(":")
            game = read_game(line[colon_idx + 2:].rstrip())
            lines.append(game)
    return lines

def is_possible(idx: int, game: list[Cubes]) -> int:
    for draw in game:
        if (draw.red > 12 or
            draw.green > 13 or
            draw.blue > 14):
            return 0
    return idx

def power_of(game: list[Cubes]) -> int:
    (red, green, blue) = (0, 0, 0)
    for draw in game:
        if draw.red > red: red = draw.red
        if draw.green > green: green = draw.green
        if draw.blue > blue: blue = draw.blue
    return red * green * blue

if __name__  == "__main__":
    # games = open_txt("test.txt")
    games = open_txt("day02.txt")
    result = 0
    for idx, game in enumerate(games, 1):
        result += is_possible(idx, game)
    print("Part 1: ", result)

    result2 = 0
    for game in games:
        result2 += power_of(game)
    print("Part 2: ", result2)
