import pytest

from common import read_input
from day15 import solve_day15_part1, solve_day15_part2, input_converter


@pytest.fixture(scope="module")
def test_input():
    return read_input("tests/inputs/day15.txt", input_converter)


def test_solve_day15_part1(test_input):
    assert 1 == solve_day15_part1(test_input)


def test_solve_day15_part2(test_input):
    assert 1 == solve_day15_part2(test_input)
