from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2018.day1.year2018day1 import solve_part1, solve_part2, input_converter


@pytest.mark.parametrize(
    "sequence, freq_hit_twice",
    [
        ([+1, +1, +1], 3),
        ([+1, +1, -2], 0),
        ([-1, -2, -3], -6),
    ],
)
def test_solve_part1(sequence, freq_hit_twice):
    solve_part1(sequence) == freq_hit_twice


@pytest.mark.parametrize(
    "sequence, freq_hit_twice",
    [
        ([+1, -1], 0),
        ([+3, +3, +4, -2, -4], 10),
        ([-6, +3, +8, +5, -6], 5),
        ([+7, +7, -2, -7, -4], 14),
    ],
)
def test_solve_part2(sequence, freq_hit_twice):
    assert solve_part2(sequence) == freq_hit_twice
