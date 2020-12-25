import math
from os.path import join, relpath, dirname
from typing import List, Tuple, Callable
from common import read_input


convert_output = str


def input_converter(input_line: str) -> convert_output:

    return str(input_line)


def solve_part1(converted_input: List[convert_output]):
    cur_pos = (0, 0, 0)

    for instruction in converted_input:
        cur_pos = execute_instruction(start_position=cur_pos, instruction=instruction)

    return manhattan_distance(cur_pos)


def execute_instruction(
    start_position: Tuple[int, int, int], instruction: str
) -> Tuple[int, int, int]:

    command, value = read_instruction(instruction)

    command_to_action = {
        "N": move(0, value),
        "S": move(0, -value),
        "E": move(value, 0),
        "W": move(-value, 0),
        "L": turn(value),
        "R": turn(-value),
        "F": forward(value),
    }

    action = command_to_action[command]

    return action(start_position)


def move(x: int, y: int) -> Callable[[Tuple[int, int, int]], Tuple[int, int, int]]:
    def execute_movement(start_pos: Tuple[int, int, int]):
        nonlocal x, y
        return start_pos[0] + x, start_pos[1] + y, start_pos[2]

    return execute_movement


def turn(degrees: int) -> Callable[[Tuple[int, int, int]], Tuple[int, int, int]]:
    def execute_turn(start_pos: Tuple[int, int, int]):
        nonlocal degrees
        return start_pos[0], start_pos[1], start_pos[2] + degrees

    return execute_turn


def forward(distance: int) -> Callable[[Tuple[int, int, int]], Tuple[int, int, int]]:
    def execute_forward(start_pos: Tuple[int, int, int]):
        nonlocal distance
        phi = start_pos[2] / 180 * math.pi
        x = math.cos(phi) * distance
        y = math.sin(phi) * distance
        return start_pos[0] + x, start_pos[1] + y, start_pos[2]

    return execute_forward


def read_instruction(instruction: str) -> Tuple[str, int]:
    return instruction[0], int(instruction[1:])


def manhattan_distance(position: Tuple[int, int, int]) -> int:

    return abs(position[0]) + abs(position[1])


def solve_part2(converted_input: List[convert_output]):
    return 1


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2020/12 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2020/12 - Part 2 is '{solve_part2(raw_input)}'")
