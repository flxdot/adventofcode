from common import read_input_groups
from day6 import solve_day6_part1


def test_solve_day6_part1():
    groups_yes_answers = read_input_groups("./tests/inputs/day6.txt", str)

    assert solve_day6_part1(groups_yes_answers) == 11
