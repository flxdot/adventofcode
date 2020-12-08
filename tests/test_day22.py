import pytest

from common import read_input
from day22 import solve_day22_part1, solve_day22_part2, input_converter


@pytest.fixture(scope="module")
def test_input():
    return read_input("tests/inputs/day22.txt", input_converter)


def test_solve_day22_part1(test_input):
    assert 1 == solve_day22_part1(test_input)


def test_solve_day22_part2(test_input):
    assert 1 == solve_day22_part2(test_input)
