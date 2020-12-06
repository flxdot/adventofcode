import pytest

from common import read_input
from day20 import solve_day20_part1, solve_day20_part2, input_converter


@pytest.fixture(scope="module")
def test_input():
    return read_input("tests/inputs/day20.txt", input_converter)


def test_solve_day20_part1(test_input):
    pass


def test_solve_day20_part2(test_input):
    pass
