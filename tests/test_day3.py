import pytest

from common import read_input
from day3 import convert_tree_map, count_on_slope


@pytest.fixture(scope="module")
def test_input():
    return read_input("./tests/inputs/day3.txt", convert_tree_map)


def test_solve_day3(test_input):
    assert count_on_slope(test_input, (1, 3)) == 7


@pytest.mark.parametrize(
    "slope, no_of_trees",
    (((1, 1), 2), ((1, 3), 7), ((1, 5), 3), ((1, 7), 4), ((2, 1), 2)),
)
def test_solve_day_part2(test_input, slope, no_of_trees):
    count_on_slope(test_input, slope) == no_of_trees
