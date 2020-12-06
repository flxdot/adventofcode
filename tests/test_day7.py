import pytest

from common import read_input
from day7 import solve_day7_part1, solve_day7_part2, input_converter


@pytest.fixture(scope="module")
def test_input():
    return read_input("tests/inputs/day7.txt", input_converter)


def test_solve_day7_part1(test_input):
    pass


def test_solve_day7_part2(test_input):
    pass
