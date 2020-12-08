import pytest

from common import read_input
from day12 import solve_day12_part1, solve_day12_part2, input_converter


@pytest.fixture(scope="module")
def test_input():
    return read_input("tests/inputs/day12.txt", input_converter)


def test_solve_day12_part1(test_input):
    assert 1 == solve_day12_part1(test_input)


def test_solve_day12_part2(test_input):
    assert 1 == solve_day12_part2(test_input)
