from os.path import join, relpath, dirname
from typing import List
from common import read_input


convert_output = List[int]


def input_converter(input_line: str) -> convert_output:
    return [int(digit) for digit in input_line]


def calculate_captcha(digit_sequence: List[int]) -> int:
    digit_sequence.append(digit_sequence[0])
    prev_num = digit_sequence[0]
    captcha_sum = 0
    for num in digit_sequence[1:]:
        if num == prev_num:
            captcha_sum += num
        prev_num = num
    return captcha_sum


def solve_part1(converted_input: List[convert_output]):
    return calculate_captcha(converted_input[0])


def solve_part2(converted_input: List[convert_output]):
    return calculate_captcha2(converted_input[0])


def calculate_captcha2(digit_sequence: List[int]) -> int:

    seq_len = len(digit_sequence)
    match_offset = seq_len / 2
    captcha_sum = 0
    for idx, num in enumerate(digit_sequence):
        match_idx = int((idx + match_offset) % seq_len)
        if num == digit_sequence[match_idx]:
            captcha_sum += num
    return captcha_sum


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2017/1 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2017/1 - Part 2 is '{solve_part2(raw_input)}'")
