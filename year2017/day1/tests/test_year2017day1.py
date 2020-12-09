from os.path import join, relpath, dirname
import pytest

from common import read_input
from year2017.day1.year2017day1 import calculate_captcha, calculate_captcha2, input_converter


@pytest.mark.parametrize(
    "digits_str,captcha_sum",
    [
        ("1122", 3),
        ("1111", 4),
        ("1234", 0),
        ("91212129", 9),
    ]
)
def test_solve_part1(digits_str, captcha_sum):

    assert calculate_captcha(input_converter(digits_str)) == captcha_sum


@pytest.mark.parametrize(
    "digits_str,captcha_sum",
    [
        ("1212", 6),
        ("1221", 0),
        ("123425", 4),
        ("123123", 12),
        ("12131415", 4),
    ]
)
def test_solve_part2(digits_str, captcha_sum):

    assert calculate_captcha2(input_converter(digits_str)) == captcha_sum
