from os.path import join, relpath, dirname
from typing import List, Tuple
from common import read_input


convert_output = Tuple[int, int, int]


def input_converter(input_line: str) -> convert_output:
    l, w, h = input_line.split("x")
    return int(l), int(w), int(h)


def calculate_wrapping_paper_surface(dimensions: convert_output) -> int:

    l, w, h = dimensions

    side_areas = [2 * l * w, 2 * w * h, 2 * h * l]

    slack = min(side_areas) / 2

    return int(sum(side_areas) + slack)


def calculate_ribbon_length(dimensions: convert_output) -> int:
    l, w, h = dimensions

    bow_length = l * w * h

    ribbon_length = sum(sorted(dimensions)[0:2]) * 2

    return bow_length + ribbon_length


def solve_part1(converted_input: List[convert_output]):
    return sum([calculate_wrapping_paper_surface(a) for a in converted_input])


def solve_part2(converted_input: List[convert_output]):
    return sum([calculate_ribbon_length(a) for a in converted_input])


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2015/2 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2015/2 - Part 2 is '{solve_part2(raw_input)}'")
