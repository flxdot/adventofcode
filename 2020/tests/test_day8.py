import pytest

from common import read_input
from day8 import solve_day8_part1, solve_day8_part2, input_converter


def test_solve_day8_part1():
    test_input = read_input("tests/inputs/day8.txt", input_converter)
    assert 5 == solve_day8_part1(test_input)


def test_solve_day8_part2():
    test_input = read_input("tests/inputs/day8_part2.txt", input_converter)
    assert 8 == solve_day8_part2(test_input)
