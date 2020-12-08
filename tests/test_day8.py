import pytest

from common import read_input
from day8 import solve_day8_part1, solve_day8_part2, input_converter


@pytest.fixture(scope="module")
def test_input():
    return read_input("tests/inputs/day8.txt", input_converter)


def test_solve_day8_part1(test_input):
    assert 5 == solve_day8_part1(test_input)


def test_solve_day8_part2(test_input):
    pass
