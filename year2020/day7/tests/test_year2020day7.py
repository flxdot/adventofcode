from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2020.day7.year2020day7 import input_converter, bag_registry, \
    solve_day7_part1, solve_day7_part2


def test_solve_part1():
    test_input = read_input(join(relpath(dirname(__file__)), "test_input.txt"),
                            input_converter)
    assert solve_day7_part1(test_input) == 4


def test_solve_part2():
    bag_registry.clear()
    test_input = read_input(join(relpath(dirname(__file__)), "test_input_part2.txt"),
                            input_converter)

    assert solve_day7_part2(test_input) == 126
