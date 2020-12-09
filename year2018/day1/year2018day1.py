from os.path import join, relpath, dirname
from typing import List
from common import read_input


input_converter = convert_output = int


def solve_part1(converted_input: List[convert_output]):
    return sum(converted_input)


def solve_part2(converted_input: List[convert_output]):

    frequency = 0
    calculated_frequencies = {}
    idx = 0
    while frequency not in calculated_frequencies:
        calculated_frequencies[frequency] = frequency
        frequency += converted_input[idx]
        idx = (idx + 1) % len(converted_input)
    return frequency


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2018/1 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2018/1 - Part 2 is '{solve_part2(raw_input)}'")
