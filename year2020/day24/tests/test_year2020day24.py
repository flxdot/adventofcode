from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2020.day24.year2020day24 import (
    solve_part1,
    solve_part2,
    input_converter,
    execute_moves,
)


@pytest.mark.parametrize(
    "directions,position", [("esew", (0, -1, 1)), ("esenee", (3, -3, 0))]
)
def test_execute_moves(directions, position):
    assert position == execute_moves(input_converter(directions))


def test_solve_part1():
    test_input = read_input(
        join(relpath(dirname(__file__)), "test_input.txt"), input_converter
    )
    assert solve_part1(test_input) == 10


@pytest.mark.parametrize(
    "black_titles,days",
    [
        (15, 1),
        (12, 2),
        (25, 3),
        (14, 4),
        (23, 5),
        (28, 6),
        (41, 7),
        (37, 8),
        (49, 9),
        (37, 10),
        (132, 20),
        (259, 30),
        (406, 40),
        (566, 50),
        (788, 60),
        (1106, 70),
        (1373, 80),
        (1844, 90),
        (2208, 100),
    ],
)
def test_solve_part2(black_titles, days):
    test_input = read_input(
        join(relpath(dirname(__file__)), "test_input.txt"), input_converter
    )
    assert solve_part2(test_input, days) == black_titles
