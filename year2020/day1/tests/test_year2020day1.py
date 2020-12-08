from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2020.day1.year2020day1 import solve_via_brute_force, solve_via_brute_force2


def test_solve_part1():
    test_input = read_input(join(relpath(dirname(__file__)), "test_input.txt"), int)
    assert 514579 == solve_via_brute_force(test_input)


def test_solve_part2():
    test_input = read_input(join(relpath(dirname(__file__)), "test_input.txt"), int)
    assert 241861950 == solve_via_brute_force2(test_input)
