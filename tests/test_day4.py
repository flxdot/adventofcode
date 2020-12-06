from common import read_input
from day4 import solve_day4, solve_day4_part2


def test_solve_day4():
    test_input = read_input("./tests/inputs/day4.txt", str)
    assert solve_day4(test_input) == 2


def test_solve_day4_part2():
    valid_input = read_input("./tests/inputs/day4_valid.txt", str)
    assert solve_day4_part2(valid_input) == 4

    invalid_input = read_input("./tests/inputs/day4_invalid.txt", str)
    assert solve_day4_part2(invalid_input) == 0
