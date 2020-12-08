from os.path import join, relpath, dirname
from typing import List
from common import read_input


convert_output = List[int]


def input_converter(input_line: str) -> convert_output:
    return [1 if char == "(" else -1 for char in input_line]


def solve_part1(converted_input: convert_output):
    return sum(converted_input)


def solve_part2(converted_input: convert_output):
    value = 0
    for idx, increment in enumerate(converted_input):
        value += increment
        if value < 0:
            return idx + 1


if __name__ == "__main__":
    raw_input = read_input(join(relpath(dirname(__file__)), "input.txt"), input_converter)

    print(f"Solution of 2015/1 - Part 1 is '{solve_part1(raw_input[0])}'")
    print(f"Solution of 2015/1 - Part 2 is '{solve_part2(raw_input[0])}'")

