from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2020.day8.year2020day8 import (
    solve_day8_part1,
    solve_day8_part2,
    input_converter,
)


def test_solve_part1():
    test_input = read_input(
        join(relpath(dirname(__file__)), "day8.txt"), input_converter
    )
    assert 5 == solve_day8_part1(test_input)


def test_solve_part2():
    test_input = read_input(
        join(relpath(dirname(__file__)), "day8_part2.txt"), input_converter
    )
    assert 8 == solve_day8_part2(test_input)
