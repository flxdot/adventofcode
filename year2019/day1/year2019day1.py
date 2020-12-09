import math
from os.path import join, relpath, dirname
from typing import List
from common import read_input


convert_output = input_converter = int


def calculate_fuel_for_mass(mass: int) -> int:
    return math.floor(mass / 3) - 2


def calculate_total_module_fuel(mass: int) -> int:

    module_fuel = calculate_fuel_for_mass(mass)
    fuel_fuel = calculate_fuel_for_mass(module_fuel)
    while fuel_fuel > 0:
        module_fuel += fuel_fuel
        fuel_fuel = calculate_fuel_for_mass(fuel_fuel)
    return module_fuel


def solve_part1(converted_input: List[convert_output]):
    return sum([calculate_fuel_for_mass(mass) for mass in converted_input])


def solve_part2(converted_input: List[convert_output]):
    return sum([calculate_total_module_fuel(mass) for mass in converted_input])


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2019/1 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2019/1 - Part 2 is '{solve_part2(raw_input)}'")
