from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2020.day9.year2020day9 import (
    solve_part2,
    input_converter,
    get_first_xmax_weakness,
)


def test_solve_part1():
    test_input = read_input(
        join(relpath(dirname(__file__)), "test_input.txt"), input_converter
    )
    assert 127 == get_first_xmax_weakness(test_input, 5)


def test_solve_part2():
    test_input = read_input(
        join(relpath(dirname(__file__)), "test_input.txt"), input_converter
    )
    assert 1 == solve_part2(test_input)
