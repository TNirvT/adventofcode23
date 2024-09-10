import re

def open_txt(filename: str) -> list[str]:
    with open(filename) as f:
        lines = []
        for line in f:
            lines.append(line.rstrip())
    return lines

def find_digits(line: str) -> int:
    first_digi = re.search(r"\d", line)
    result_str = first_digi.group(0)
    second_digi = re.search(r"\d", line[::-1])
    return int(result_str + second_digi.group(0))

spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
forward_dict = {}
reversed_dict = {}
for count, word in enumerate(spelled, 1):
    forward_dict[word] = str(count)
    reversed_dict[word[::-1]] = str(count)
forward_pattern = r"\d|" + "|".join(spelled)
reversed_pattern = r"\d|" + "|".join(reversed_dict.keys())

def find_part2(line: str) -> int:
    first_digi = re.search(forward_pattern, line)
    result_str = first_digi.group(0)
    if first_digi.group(0) in spelled:
        result_str = forward_dict[first_digi.group(0)]
    second_digi = re.search(reversed_pattern, line[::-1])
    if second_digi.group(0) in reversed_dict.keys():
        return int(result_str + reversed_dict[second_digi.group(0)])
    return int(result_str + second_digi.group(0))

if __name__  == "__main__":
    # lines = open_txt("test.txt")
    lines = open_txt("day01.txt")
    # result = 0
    # for line in lines:
    #     result += find_digits(line)
    # print("Part 1: ", result)

    result2 = 0
    for line in lines:
        result2 += find_part2(line)
    print("Part 2: ", result2)
