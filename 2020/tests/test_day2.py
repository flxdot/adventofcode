from common import read_input
from day2 import (
    solve_day2,
    validate_password_part1,
    validate_password_part2,
    convert_line_of_input,
)


def test_solve_day2():

    test_input = read_input("./tests/inputs/day2.txt", convert_line_of_input)

    assert solve_day2(test_input, validate_password_part1) == 2
    assert solve_day2(test_input, validate_password_part2) == 1
