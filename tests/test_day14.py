import pytest

from common import read_input
from day14 import solve_day14_part1, solve_day14_part2, input_converter


@pytest.fixture(scope="module")
def test_input():
    return read_input("tests/inputs/day14.txt", input_converter)


def test_solve_day14_part1(test_input):
    pass


def test_solve_day14_part2(test_input):
    pass
