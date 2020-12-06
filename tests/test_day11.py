import pytest

from common import read_input
from day11 import solve_day11_part1, solve_day11_part2, input_converter


@pytest.fixture(scope="module")
def test_input():
    return read_input("tests/inputs/day11.txt", input_converter)


def test_solve_day11_part1(test_input):
    pass


def test_solve_day11_part2(test_input):
    pass
