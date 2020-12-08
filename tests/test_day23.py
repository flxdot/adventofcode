import pytest

from common import read_input
from day23 import solve_day23_part1, solve_day23_part2, input_converter


@pytest.fixture(scope="module")
def test_input():
    return read_input("tests/inputs/day23.txt", input_converter)


def test_solve_day23_part1(test_input):
    assert 1 == solve_day23_part1(test_input)


def test_solve_day23_part2(test_input):
    assert 1 == solve_day23_part2(test_input)
