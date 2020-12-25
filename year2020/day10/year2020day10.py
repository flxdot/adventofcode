from os.path import join, relpath, dirname
from typing import List
from common import read_input


convert_output = int


def input_converter(input_line: str) -> convert_output:
    return int(input_line)


def solve_part1(converted_input: List[convert_output]):

    sorted_adapter_list = sort_and_complete_adapters(converted_input)

    jolt_diff_count = {1: 0, 2: 0, 3: 0}
    for low_jolt, high_jolt in zip(sorted_adapter_list[:-1], sorted_adapter_list[1:]):
        cur_diff = high_jolt - low_jolt
        jolt_diff_count[cur_diff] += 1

    return jolt_diff_count[1] * jolt_diff_count[3]


def sort_and_complete_adapters(adapter_ratings: List[int]) -> List[int]:
    return [0] + sorted(adapter_ratings) + [max(adapter_ratings) + 3]


def solve_part2(converted_input: List[convert_output]):
    sorted_adapter_list = sort_and_complete_adapters(converted_input)

    distinct_adapter_configurations = []
    get_next_combinations(
        sorted_adapter_list, combinations=distinct_adapter_configurations
    )

    return len(distinct_adapter_configurations)


def get_next_combinations(
    sorted_adapter_list: List[int],
    current_rating: int = 0,
    combinations: List[List[int]] = [],
    combination: List[int] = [],
):

    next_suiting_ratings = [
        rating
        for rating in sorted_adapter_list
        if current_rating < rating <= current_rating + 3
    ]

    if current_rating == max(sorted_adapter_list):
        combinations.append(combination)
        return

    for rating in next_suiting_ratings:
        get_next_combinations(
            sorted_adapter_list=sorted_adapter_list,
            current_rating=rating,
            combination=combination[:] + [rating],
            combinations=combinations,
        )


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2020/10 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2020/10 - Part 2 is '{solve_part2(raw_input)}'")
