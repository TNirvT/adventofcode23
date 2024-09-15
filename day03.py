import re

def open_txt(filename: str) -> list[str]:
    with open(filename) as f:
        lines = []
        for line in f:
            lines.append(line.rstrip())
    return lines

def one_line_symbols(line: str) -> set[int]:
    locations = set()
    for idx, char in enumerate(line):
        if char == "." or char.isalnum():
            continue
        locations.add(idx)
    return locations

def one_line_sum(line_idx: int, line: str, symbol_locations: list[set[int]]) -> int:
    one_line = 0
    for m in re.finditer(r"\d+", line):
        if m.start() - 1 in symbol_locations[line_idx] or m.end() in symbol_locations[line_idx]:
            one_line += int(m.group(0))
            continue
        # check previous line
        if line_idx < 0:
            continue
        if set(range(m.start() - 1, m.end() + 1)).intersection(symbol_locations[line_idx - 1]):
            one_line += int(m.group(0))
            continue
        # check next line
        if line_idx == len(symbol_locations) - 1:
            continue
        if set(range(m.start() - 1, m.end() + 1)).intersection(symbol_locations[line_idx + 1]):
            one_line += int(m.group(0))
    return one_line

def gear_ratio(lines: list[str], line_idx: int, idx: int) -> int:
    (first_gear, second_gear) = (0, 0)
    # check previous line
    if line_idx > 0:
        for m in re.finditer(r"\d+", lines[line_idx - 1]):
            if m.end() < idx or m.start() > idx + 1:
                continue
            if second_gear:
                return 0
            if first_gear:
                second_gear = int(m.group(0))
                continue
            first_gear = int(m.group(0))
    # check same line
    if idx > 0 and lines[line_idx][idx - 1].isdecimal():
        if second_gear:
            return 0
        m = re.match(r"\d+", lines[line_idx][:idx][::-1])
        if first_gear:
            second_gear = int(m.group(0)[::-1])
        if not first_gear:
            first_gear = int(m.group(0)[::-1])
    if idx < len(lines[line_idx]) - 1 and lines[line_idx][idx + 1].isdecimal():
        if second_gear:
            return 0
        m = re.match(r"\d+", lines[line_idx][idx + 1:])
        if first_gear:
            second_gear = int(m.group(0))
        if not first_gear:
            first_gear = int(m.group(0))
    # check next line
    if line_idx < len(lines) - 1:
        for m in re.finditer(r"\d+", lines[line_idx + 1]):
            if m.end() < idx or m.start() > idx + 1:
                continue
            if second_gear:
                return 0
            if first_gear:
                second_gear = int(m.group(0))
                continue
            first_gear = int(m.group(0))
    return first_gear * second_gear

def gear_ratio_sum(lines: list[str]):
    result = 0
    for line_idx, line in enumerate(lines):
        for idx, char in enumerate(line):
            if char == "*":
                result += gear_ratio(lines, line_idx, idx)
    return result

if __name__ == "__main__":
    # lines = open_txt("test.txt")
    lines = open_txt("day03.txt")
    result = 0
    symbol_locations = []
    for line in lines:
        symbol_locations.append(one_line_symbols(line))
    for line_idx, line in enumerate(lines):
        result += one_line_sum(line_idx, line, symbol_locations)
    print("Part 1: ", result)
    result_part_two = gear_ratio_sum(lines)
    print("Part 2: ", result_part_two)
