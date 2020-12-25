from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2020.day10.year2020day10 import solve_part1, solve_part2, input_converter


@pytest.mark.parametrize(
    "test_file,combinations",
    [
        ("test_input_small.txt", 35),
        ("test_input_large.txt", 220),
    ],
)
def test_solve_part1(test_file, combinations):
    test_input = read_input(
        join(relpath(dirname(__file__)), test_file), input_converter
    )
    assert combinations == solve_part1(test_input)


@pytest.mark.parametrize(
    "test_file,combinations",
    [
        ("test_input_very_small.txt", 4),
        ("test_input_small.txt", 8),
        ("test_input_large.txt", 19208),
    ],
)
def test_solve_part2(test_file, combinations):
    test_input = read_input(
        join(relpath(dirname(__file__)), test_file), input_converter
    )
    assert combinations == solve_part2(test_input)
