from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2020.day2.year2020day2 import (
    input_converter,
    validate_password_part1,
    validate_password_part2,
    solve_day2,
)


def test_solve_part1():
    test_input = read_input(
        join(relpath(dirname(__file__)), "test_input.txt"), input_converter
    )
    assert 2 == solve_day2(test_input, validate_password_part1)


def test_solve_part2():
    test_input = read_input(
        join(relpath(dirname(__file__)), "test_input.txt"), input_converter
    )
    assert 1 == solve_day2(test_input, validate_password_part2)
