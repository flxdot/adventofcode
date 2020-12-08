import os

from tools.fetch_data import get_task_description, get_task_input


def write_day(year: int, day: int):
    print(f"{year}/{day}", end="")

    write_solution_file(year, day)
    print(".", end="")
    write_test_file(year, day)
    print(".", end="")
    write_input_file(year, day)
    print(".", end="")
    write_test_input_file(year, day)
    print(".")


def write_solution_file(year: int, day: int):
    name = f"day{day}"

    path = str(year)
    main_file = f"{name}.py"

    full_file_path = os.path.abspath(os.path.join(path, main_file))
    if not os.path.isdir(os.path.dirname(full_file_path)):
        os.makedirs(os.path.dirname(full_file_path))

    input_file = os.path.join(str(year), "inputs", f"{name}.txt")

    with open(full_file_path, "w") as writer:
        writer.write(f'''"""
{get_task_description(year, day)}
"""

from typing import List
from common import read_input


convert_output = str


def input_converter(input_line: str) -> convert_output:
    return str(input_line)


def solve_{name}_part1(converted_input: List[convert_output]):
    return 1


def solve_{name}_part2(converted_input: List[convert_output]):
    return 1


if __name__ == "__main__":
    raw_input = read_input("{input_file}", input_converter)

    print(f"Solution of Day 1 - Part 1 is '{{solve_{name}_part1(raw_input)}}'")
    print(f"Solution of Day 1 - Part 2 is '{{solve_{name}_part2(raw_input)}}'")

''')


def write_test_file(year: int, day: int):
    name = f"day{day}"

    path = os.path.join(str(year), "tests")
    file_name = f"test_{name}.py"

    full_file_path = os.path.abspath(os.path.join(path, file_name))
    if not os.path.isdir(os.path.dirname(full_file_path)):
        os.makedirs(os.path.dirname(full_file_path))

    test_input_file = os.path.join(str(year), "tests", "inputs", f"{name}.txt")

    with open(full_file_path, "w") as writer:
        writer.write(f'''import pytest

        from common import read_input
        from {name} import solve_{name}_part1, solve_{name}_part2, input_converter


        def test_solve_{name}_part1(test_input):
            test_input = read_input("{test_input_file}", input_converter)
            assert 1 == solve_{name}_part1(test_input)


        def test_solve_{name}_part2(test_input):
            test_input = read_input("{test_input_file}", input_converter)
            assert 1 == solve_{name}_part2(test_input)
        ''')


def write_input_file(year: int, day: int):
    name = f"day{day}"

    path = os.path.join(str(year), "inputs")
    file_name = f"{name}.txt"

    full_file_path = os.path.abspath(os.path.join(path, file_name))
    if not os.path.isdir(os.path.dirname(full_file_path)):
        os.makedirs(os.path.dirname(full_file_path))

    with open(full_file_path, "w") as writer:
        writer.write(get_task_input(year, day))


def write_test_input_file(year: int, day: int):
    name = f"day{day}"

    path = os.path.join(str(year), "tests", "inputs")
    file_name = f"{name}.txt"

    full_file_path = os.path.abspath(os.path.join(path, file_name))
    if not os.path.isdir(os.path.dirname(full_file_path)):
        os.makedirs(os.path.dirname(full_file_path))

    with open(full_file_path, "w") as writer:
        writer.write(get_task_input(year, day))


if __name__ == "__main__":
    for year in range(2015, 2020):
        for day in range(1, 25):
            write_day(year, day)



