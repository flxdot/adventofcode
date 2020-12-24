import os

from tools.fetch_data import get_task_description, get_task_input, get_task_url


def write_day(year: int, day: int):
    print(f"{year}/{day}", end="")

    day_init_file = os.path.join(f"year{year}", f"day{day}", "__init__.py")
    write_file(day_init_file, "")
    print(".", end="")

    tests_init_file = os.path.join(f"year{year}", f"day{day}", "tests", "__init__.py")
    write_file(tests_init_file, "")
    print(".", end="")

    write_readme_file(year, day)
    print(".", end="")
    write_solution_file(year, day)
    print(".", end="")
    write_test_file(year, day)
    print(".", end="")
    write_input_file(year, day)
    print(".", end="")
    write_test_input_file(year, day)
    print(".")


def write_file(path: str, content: str):

    if not os.path.isdir(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, "w") as writer:
        writer.write(content)


def write_readme_file(year: int, day: int):
    name = f"day{day}"
    path = os.path.join(f"year{year}", name)
    file_name = f"README.md"

    read_me = f"""# Advent of Code {year} - Day {day}

Solution for this day: [year{year}day{day}.py](year{year}day{day}.py)

My input for this day: [input.txt](input.txt)

{get_task_description(year, day)}

Source: [{get_task_url(year, day)}]({get_task_url(year, day)})
"""

    write_file(os.path.join(path, file_name), read_me)


def write_solution_file(year: int, day: int):
    name = f"day{day}"
    path = os.path.join(f"year{year}", name)
    file_name = f"year{year}day{day}.py"

    if not os.path.isdir(path):
        os.makedirs(path)

    with open(os.path.join(path, file_name), "w") as writer:
        writer.write(
            f"""from os.path import join, relpath, dirname
from typing import List
from common import read_input


convert_output = str


def input_converter(input_line: str) -> convert_output:
    return str(input_line)


def solve_part1(converted_input: List[convert_output]):
    return 1


def solve_part2(converted_input: List[convert_output]):
    return 1


if __name__ == "__main__":
    raw_input = read_input(join(relpath(dirname(__file__)), "input.txt"), input_converter)

    print(f"Solution of {year}/{day} - Part 1 is '{{solve_part1(raw_input)}}'")
    print(f"Solution of {year}/{day} - Part 2 is '{{solve_part2(raw_input)}}'")

"""
        )


def write_test_file(year: int, day: int):
    name = f"day{day}"
    path = os.path.join(f"year{year}", name, "tests")
    file_name = f"test_year{year}day{day}.py"

    if not os.path.isdir(path):
        os.makedirs(path)

    with open(os.path.join(path, file_name), "w") as writer:
        writer.write(
            f"""from os.path import join, relpath, dirname
import pytest

from common import read_input
from year{year}.{name}.year{year}day{day} import solve_part1, solve_part2, input_converter


def test_solve_part1():
    test_input = read_input(join(relpath(dirname(__file__)), "test_input.txt"), input_converter)
    assert solve_part1(test_input) == 1


def test_solve_part2():
    test_input = read_input(join(relpath(dirname(__file__)), "test_input.txt"), input_converter)
    assert solve_part2(test_input) == 1
"""
        )


def write_input_file(year: int, day: int):

    name = f"day{day}"
    path = os.path.join(f"year{year}", name)
    file_name = f"input.txt"

    if not os.path.isdir(path):
        os.makedirs(path)

    with open(os.path.join(path, file_name), "w") as writer:
        writer.write(get_task_input(year, day))


def write_test_input_file(year: int, day: int):
    name = f"day{day}"
    path = os.path.join(f"year{year}", name, "tests")
    file_name = f"test_input.txt"

    if not os.path.isdir(path):
        os.makedirs(path)

    with open(os.path.join(path, file_name), "w") as writer:
        writer.write("")


if __name__ == "__main__":
    for year in range(2015, 2020):

        year_init_file = os.path.join(f"year{year}", "__init__.py")
        write_file(year_init_file, "")

        for day in range(1, 25):
            write_day(year, day)
