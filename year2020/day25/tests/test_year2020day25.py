from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2020.day25.year2020day25 import (
    solve_part1,
    solve_part2,
    input_converter,
    find_loop_size,
    calculate_public_key,
)


@pytest.mark.parametrize("public_key, loop_size", [(5764801, 8), (17807724, 11)])
def test_find_loop_size(public_key, loop_size):
    assert find_loop_size(7, public_key) == loop_size


@pytest.mark.parametrize(
    "public_key,loop_size,encryption_key",
    [(17807724, 8, 14897079), (5764801, 11, 14897079)],
)
def test_calculate_public_key(public_key, loop_size, encryption_key):
    assert calculate_public_key(loop_size, public_key) == encryption_key


def test_solve_part2():
    test_input = read_input(
        join(relpath(dirname(__file__)), "test_input.txt"), input_converter
    )
    assert solve_part2(test_input) == 1
