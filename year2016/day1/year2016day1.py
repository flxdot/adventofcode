import math
from os.path import join, relpath, dirname
from typing import List, Tuple
from common import read_input


convert_output = List[str]


class GridWalker:
    def __init__(self):

        self._current_pos = [0, 0]
        self._heading = math.pi / 2

    @property
    def position(self):
        return self._current_pos

    @property
    def distance_from_home(self):
        return int(abs(self._current_pos[0]) + abs(self._current_pos[1]))

    def __repr__(self):
        return (
            f"Self @ {self.position[0]},{self.position[1]} - {self.distance_from_home}"
        )

    def walk(self, direction: str):

        heading, distance = self._convert_direction(direction)

        self._heading += heading

        self._current_pos[0] += int(math.cos(self._heading) * distance)
        self._current_pos[1] += int(math.sin(self._heading) * distance)

    @staticmethod
    def _convert_direction(direction: str) -> Tuple[float, int]:
        """Converts a direction into a heading and distance."""

        direction_to_heading = {"L": math.pi / 2, "R": -math.pi / 2}

        return direction_to_heading[direction[0]], int(direction[1])


def input_converter(input_line: str) -> convert_output:
    return input_line.split(", ")


def solve_part1(converted_input: List[convert_output]):

    walker = GridWalker()
    for direction in converted_input[0]:
        walker.walk(direction)
    return walker.distance_from_home


def solve_part2(converted_input: List[convert_output]):
    return 1


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2016/1 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2016/1 - Part 2 is '{solve_part2(raw_input)}'")
