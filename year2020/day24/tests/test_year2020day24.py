from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2020.day24.year2020day24 import solve_part1, solve_part2, input_converter, execute_moves


@pytest.mark.parametrize(
    "directions,position",
    [
        ("esew", (0, -1, 1)),
        ("esenee", (3, -3, 0))
    ]
)
def test_execute_moves(directions, position):
    assert position == execute_moves(input_converter(directions))


def test_solve_part1():
    test_input = read_input(join(relpath(dirname(__file__)), "test_input.txt"), input_converter)
    assert 10 == solve_part1(test_input)


def test_solve_part2():
    test_input = read_input(join(relpath(dirname(__file__)), "test_input.txt"), input_converter)
    assert 1 == solve_part2(test_input)
