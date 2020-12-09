from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2016.day1.year2016day1 import solve_part1, solve_part2, input_converter


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("R2, L3", 5),
        ("R2, R2, R2", 2),
        ("R5, L5, R5, R3", 12)
    ]
)
def test_solve_part1(test_input, expected):
    assert solve_part1([input_converter(test_input)]) == expected


def test_solve_part2():
    test_input = read_input(
        join(relpath(dirname(__file__)), "test_input.txt"), input_converter
    )
    assert 1 == solve_part2(test_input)
