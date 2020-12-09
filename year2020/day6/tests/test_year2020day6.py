from os.path import join, relpath, dirname
import pytest

from common import read_input_groups
from year2020.day6.year2020day6 import solve_day6_part1, solve_day6_part2


def test_solve_part1():
    test_input = read_input_groups(
        join(relpath(dirname(__file__)), "test_input.txt"), str
    )
    assert 11 == solve_day6_part1(test_input)


def test_solve_part2():
    test_input = read_input_groups(
        join(relpath(dirname(__file__)), "test_input.txt"), str
    )
    assert 6 == solve_day6_part2(test_input)
