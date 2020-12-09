from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2015.day1.year2015day1 import solve_part1, solve_part2, input_converter


@pytest.mark.parametrize(
    "test_input,expected_result",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_solve_part1(test_input, expected_result):
    assert expected_result == solve_part1(input_converter(test_input))


@pytest.mark.parametrize("test_input,expected_result", [(")", 1), ("()())", 5)])
def test_solve_part2(test_input, expected_result):
    assert expected_result == solve_part2(input_converter(test_input))
