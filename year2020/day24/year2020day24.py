from os.path import join, relpath, dirname
from typing import List, Tuple
from common import read_input


convert_output = List[Tuple[int, int, int]]


def input_converter(input_line: str) -> convert_output:
    direction_to_moves = {
        'ne': (1, 0, -1),
        'e': (1, -1, 0),
        'se': (0, -1, 1),
        'nw': (0, 1, -1),
        'sw': (-1, 0, 1),
        'w': (-1, 1, 0),
    }

    moves = []
    while len(input_line) > 0:
        try:
            moves.append(direction_to_moves[input_line[:1]])
            input_line = input_line[1:]
        except KeyError:
            moves.append(direction_to_moves[input_line[:2]])
            input_line = input_line[2:]

    return moves


def execute_moves(moves: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:

    position = (0, 0, 0)
    for move in moves:
        position = (
            position[0] + move[0],
            position[1] + move[1],
            position[2] + move[2],
        )
    return position


def solve_part1(converted_input: List[convert_output]):

    title_map = {}
    for moves in converted_input:
        title_pos = execute_moves(moves)
        title_map[title_pos] = not title_map.get(title_pos, False)

    return sum([1 for is_black in title_map.values() if is_black])


def solve_part2(converted_input: List[convert_output]):
    return 1


if __name__ == "__main__":
    raw_input = read_input(join(relpath(dirname(__file__)), "input.txt"), input_converter)

    print(f"Solution of 2020/24 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2020/24 - Part 2 is '{solve_part2(raw_input)}'")

