from os.path import join, relpath, dirname
from typing import List
from common import read_input


convert_output = int


def input_converter(input_line: str) -> convert_output:
    return int(input_line)


def solve_part1(converted_input: List[convert_output]):
    try:
        return calculate_encryption_key(converted_input[0], converted_input[1])
    except AssertionError:
        return calculate_encryption_key(converted_input[1], converted_input[0])


def calculate_public_key(loop_size: int, subject_number: int) -> int:

    value = 1
    for _ in range(loop_size):
        value = transform_subject_number(subject_number, value)
    return value


def transform_subject_number(subject_number: int, value: int = 1) -> int:
    value *= subject_number
    return value % 20201227


def find_loop_size(subject_number: int, public_key: int) -> int:
    loop_size = 0
    calc_public_key = 1
    while calc_public_key != public_key:
        calc_public_key = transform_subject_number(subject_number, calc_public_key)
        loop_size += 1

    return loop_size


def calculate_encryption_key(
    public_key_door: int, public_key_card: int, subject_number: int = 7
) -> int:

    card_loop_size = find_loop_size(subject_number, public_key_card)
    door_loop_size = find_loop_size(subject_number, public_key_door)

    door_encryption_key = calculate_public_key(card_loop_size, public_key_door)
    card_encryption_key = calculate_public_key(door_loop_size, public_key_card)

    assert door_encryption_key == card_encryption_key

    return door_encryption_key


def solve_part2(converted_input: List[convert_output]):
    return 1


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2020/25 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2020/25 - Part 2 is '{solve_part2(raw_input)}'")
