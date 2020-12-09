from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2016.day13.year2016day13 import solve_part1, solve_part2, input_converter


def test_solve_part1():
    test_input = read_input(
        join(relpath(dirname(__file__)), "test_input.txt"), input_converter
    )
    assert 1 == solve_part1(test_input)


def test_solve_part2():
    test_input = read_input(
        join(relpath(dirname(__file__)), "test_input.txt"), input_converter
    )
    assert 1 == solve_part2(test_input)
