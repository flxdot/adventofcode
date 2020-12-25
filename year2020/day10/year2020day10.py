from os.path import join, relpath, dirname
from typing import List
from common import read_input


convert_output = int


def input_converter(input_line: str) -> convert_output:
    return int(input_line)


def solve_part1(converted_input: List[convert_output]):

    sorted_adapter_list = sorted(converted_input)
    sorted_adapter_list = [0] + sorted_adapter_list + [max(sorted_adapter_list) + 3]

    jolt_diff_count = {1: 0, 2: 0, 3: 0}
    for low_jolt, high_jolt in zip(sorted_adapter_list[:-1], sorted_adapter_list[1:]):
        cur_diff = high_jolt - low_jolt
        jolt_diff_count[cur_diff] += 1

    return jolt_diff_count[1] * jolt_diff_count[3]


def solve_part2(converted_input: List[convert_output]):
    return 1


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2020/10 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2020/10 - Part 2 is '{solve_part2(raw_input)}'")
