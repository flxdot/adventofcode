from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2020.day4.year2020day4 import solve_day4, solve_day4_part2


def test_solve_part1():
    test_input = read_input(join(relpath(dirname(__file__)), "test_input.txt"), str)
    assert 2 == solve_day4(test_input)


def test_solve_part2():
    valid_input = read_input(
        join(relpath(dirname(__file__)), "test_input_part2_valid.txt"), str
    )
    assert solve_day4_part2(valid_input) == 4

    invalid_input = read_input(
        join(relpath(dirname(__file__)), "test_input_part2_invalid.txt"), str
    )
    assert solve_day4_part2(invalid_input) == 0
