from typing import NamedTuple

class Mapping(NamedTuple):
    destination: int
    source: int
    range: int

def open_txt(filename: str) -> tuple[list[int], list[list[Mapping]]]:
    with open(filename) as f:
        map_list = []
        flagged = False
        for line in f:
            if line.startswith("\n") and flagged:
                flagged = False
                continue

            if line.startswith("seeds:"):
                seeds = [int(x) for x in line[6:].split()]
                continue

            if line.endswith("map:\n"):
                flagged = True
                map_list.append([])
                continue

            if flagged:
                map_list[-1].append(Mapping._make(int(x) for x in line.split()))

    return (seeds, map_list)

def mapping_child(source: int, mappings: list[Mapping]) -> int:
    for mapping in mappings:
        if source >= mapping.source and source < mapping.source + mapping.range:
            return mapping.destination + source - mapping.source
    return source

def find_location(seed: int, map_list: list[list[Mapping]]) -> int:
    destination = seed
    for mappings in map_list:
        destination = mapping_child(destination, mappings)
    return destination

if __name__ == "__main__":
    # (seeds, map_list) = open_txt("test.txt")
    (seeds, map_list) = open_txt("day05.txt")
    locations = []
    for seed in seeds:
        locations.append(find_location(seed, map_list))
    print("Part 1: ", min(locations))
