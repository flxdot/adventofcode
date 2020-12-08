import pytest

from common import read_input
from day7 import solve_day7_part1, solve_day7_part2, input_converter, bag_registry


@pytest.fixture(scope="module")
def test_input():
    bag_registry.clear()
    return read_input("tests/inputs/day7.txt", input_converter)


def test_solve_day7_part1(test_input):
    assert solve_day7_part1(test_input) == 4


def test_solve_day7_part2():
    bag_registry.clear()
    test_input = read_input("tests/inputs/day7_part2.txt", input_converter)

    assert solve_day7_part2(test_input) == 126
