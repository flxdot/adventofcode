from os.path import join, relpath, dirname
from typing import List
from common import read_input


convert_output = str


def input_converter(input_line: str) -> convert_output:
    return str(input_line)


def solve_part1(converted_input: List[convert_output]):
    return 1


def solve_part2(converted_input: List[convert_output]):
    return 1


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2019/6 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2019/6 - Part 2 is '{solve_part2(raw_input)}'")
