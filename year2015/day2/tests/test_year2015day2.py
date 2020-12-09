from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2015.day2.year2015day2 import (
    input_converter,
    calculate_wrapping_paper_surface,
    calculate_ribbon_length,
)


@pytest.mark.parametrize("dimensions, area", [("2x3x4", 58), ("1x1x10", 43)])
def test_solve_part1(dimensions, area):
    assert area == calculate_wrapping_paper_surface(input_converter(dimensions))


@pytest.mark.parametrize("dimensions, ribbon_length", [("2x3x4", 34), ("1x1x10", 14)])
def test_solve_part2(dimensions, ribbon_length):
    assert ribbon_length == calculate_ribbon_length(input_converter(dimensions))
