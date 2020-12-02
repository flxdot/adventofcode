"""
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""

from dataclasses import dataclass
from typing import Tuple, List

from common import read_input


@dataclass
class PasswordPolicy:
    letter: str
    min_occurrence: int
    max_occurrence: int

    @classmethod
    def from_string(cls, policy_string: str) -> "PasswordPolicy":
        """Converts a password policy into the actual dataclass"""

        occurrences, letter = policy_string.split()
        min_occurrence, max_occurrence = occurrences.split("-")

        return cls(
            letter=letter,
            min_occurrence=int(min_occurrence),
            max_occurrence=int(max_occurrence),
        )

    def __repr__(self):
        return f"{self.min_occurrence}-{self.max_occurrence} {self.letter}"


def convert_line_of_input(line: str) -> Tuple[PasswordPolicy, str]:
    """Convert the input line into the password policy and the actual password"""

    policy_string, password = line.split(":")

    return PasswordPolicy.from_string(policy_string), password.strip()


def validate_password(policy: PasswordPolicy, password: str) -> bool:
    """Validates the password with the policy."""

    letter_occurrences = sum([letter == policy.letter for letter in password])

    return policy.min_occurrence <= letter_occurrences <= policy.max_occurrence


def solve_day2(day2_data: List[Tuple[PasswordPolicy, str]]) -> int:
    """Counts the amount of passwords not matching the policy."""

    validations = map(lambda case: validate_password(case[0], case[1]), day2_data)

    return sum(validations)


if __name__ == "__main__":
    converted_inputs = read_input("./inputs/day2.txt", convert_line_of_input)

    print(f"Solution of day2 is '{solve_day2(converted_inputs)}'")
