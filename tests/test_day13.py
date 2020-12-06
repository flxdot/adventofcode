import pytest

from common import read_input
from day13 import solve_day13_part1, solve_day13_part2, input_converter


@pytest.fixture(scope="module")
def test_input():
    return read_input("tests/inputs/day13.txt", input_converter)


def test_solve_day13_part1(test_input):
    pass


def test_solve_day13_part2(test_input):
    pass
