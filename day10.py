"""

"""

from typing import List
from common import read_input


convert_output = str


def input_converter(input_line: str) -> convert_output:
    return str(input_line)


def solve_day10_part1(converted_input: List[convert_output]):
    pass


def solve_day10_part2(converted_input: List[convert_output]):
    pass


if __name__ == "__main__":
    raw_input = read_input("inputs/day10.txt", input_converter)

    print(f"Solution of Day 1 - Part 1 is '{solve_day10_part1(raw_input)}'")
    print(f"Solution of Day 1 - Part 2 is '{solve_day10_part2(raw_input)}'")
