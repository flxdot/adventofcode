import pytest

from common import read_input
from day1 import solve_via_dict2, solve_via_brute_force2


@pytest.fixture(scope="module")
def test_input():
    return read_input("./tests/inputs/day1.txt", int)


def test_solve_via_dict2(test_input):
    assert solve_via_dict2(test_input) == 514579


def test_solve_via_brute_force2(test_input):
    assert solve_via_brute_force2(test_input) == 241861950
