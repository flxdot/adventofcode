"""
--- Day 4: Passport Processing ---

You arrive at the airport only to realize that you grabbed your North Pole Credentials instead
of your passport. While these documents are extremely similar, North Pole Credentials aren't
issued by a country and therefore aren't actually valid documentation for travel in most of
the world.

It seems like you're not the only one having problems, though; a very long line has formed for
the automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of
these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which
passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented
as a sequence of key:value pairs separated by spaces or newlines. Passports are separated
by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present.

The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from
North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the
system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing
any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as
optional. In your batch file, how many passports are valid?
"""
import re
from dataclasses import dataclass, fields, field
from typing import List, Union, Any

from common import read_input


class ValidationError(Exception):
    pass


def value_in_range(
    value: Union[str, int, float], min: Union[int, float], max: Union[int, float]
) -> bool:
    return value is not None and min <= float(value) <= max


def validate_height(height_str: str) -> bool:
    if height_str is None:
        return False
    if height_str.endswith("cm"):
        return value_in_range(float(height_str.replace("cm", "")), 150, 193)
    elif height_str.endswith("in"):
        return value_in_range(float(height_str.replace("in", "")), 59, 76)
    return False


def validate_web_color(color_str: str) -> bool:
    if color_str is None:
        return False

    return re.compile("#[0-9a-f]{6}").match(color_str) is not None


def is_one_of(choice: Any, choices: List[Any]) -> bool:
    if choice is None:
        return False
    return choice in choices


@dataclass
class Passport:
    byr: str = field(
        default=None,
        metadata={
            "validator": value_in_range,
            "validator_kwargs": {"min": 1920, "max": 2002},
        },
    )
    iyr: str = field(
        default=None,
        metadata={
            "validator": value_in_range,
            "validator_kwargs": {"min": 2010, "max": 2020},
        },
    )
    eyr: str = field(
        default=None,
        metadata={
            "validator": value_in_range,
            "validator_kwargs": {"min": 2020, "max": 2030},
        },
    )
    hgt: str = field(
        default=None,
        metadata={"validator": validate_height},
    )
    hcl: str = field(
        default=None,
        metadata={"validator": validate_web_color},
    )
    ecl: str = field(
        default=None,
        metadata={
            "validator": is_one_of,
            "validator_kwargs": {
                "choices": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            },
        },
    )
    pid: str = field(
        default=None,
        metadata={
            "validator": lambda value: value is not None and len(value) == 9,
        },
    )
    cid: str = field(
        default=None,
        metadata={
            "validator": lambda value: True,
        },
    )

    @property
    def is_valid(self):
        fields_to_validate = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        return all([getattr(self, field) is not None for field in fields_to_validate])

    @property
    def is_type_valid(self):
        for field in fields(self):
            field_value = getattr(self, field.name)
            if "validator" in field.metadata:
                validator = field.metadata["validator"]
                validator_params = field.metadata.get("validator_kwargs", {})
                if not validator(field_value, **validator_params):
                    return False
        return True


def extract_passports(raw_data: List[str]) -> List[Passport]:
    """Converts the batch of passport information in the to list of passport objects."""

    passport_data_sets = combine_consecutive_lines(raw_data)

    passports = []
    for data_set in passport_data_sets:
        kwargs = {}
        for attrib_str in data_set.split():
            key, value = attrib_str.split(":")
            kwargs[key] = value
        passports.append(Passport(**kwargs))

    return passports


def combine_consecutive_lines(raw_data: List[str]) -> List[str]:
    """Combine consecutive lines into one string."""

    password_data_sets = []
    current_data_set = []
    for line in raw_data:
        line = line.strip()
        if line:
            current_data_set.append(line)
        else:
            password_data_sets.append(" ".join(current_data_set))
            current_data_set = []
    password_data_sets.append(" ".join(current_data_set))

    return password_data_sets


def solve_day4(raw_data: List[str]):
    passports = extract_passports(raw_data)

    return sum([passport.is_valid for passport in passports])


def solve_day4_part2(raw_data: List[str]):
    passports = extract_passports(raw_data)

    return sum([passport.is_type_valid for passport in passports])


if __name__ == "__main__":
    raw_data = read_input("./inputs/day4.txt", str)

    print(solve_day4(raw_data))
    print(solve_day4_part2(raw_data))
