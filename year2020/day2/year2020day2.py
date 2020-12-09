"""
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down to the
coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's
wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't
have been allowed by the Official Toboggan Corporate Policy that was in effect when they
were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords
(according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates
the lowest and highest number of times a given letter must appear for the password to be
valid. For example, 1-3 a means that the password must contain a at least 1 time and at
most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains
no instances of b, but needs at least 1. The first and third passwords are valid: they
contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the
Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy
rules from his old job at the sled rental place down the street! The Official Toboggan
Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first
character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies
have no concept of "index zero"!) Exactly one of these positions must contain the given letter.
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""

from dataclasses import dataclass
from os.path import join, relpath, dirname
from typing import Tuple, List, Callable

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


input_converter = convert_line_of_input


def validate_password_part1(policy: PasswordPolicy, password: str) -> bool:
    """Validates the password with the policy."""

    letter_occurrences = sum([letter == policy.letter for letter in password])

    return policy.min_occurrence <= letter_occurrences <= policy.max_occurrence


def validate_password_part2(policy: PasswordPolicy, password: str) -> bool:
    """Validates the password with the policy."""

    return (
        password[policy.min_occurrence - 1] == policy.letter
        or password[policy.max_occurrence - 1] == policy.letter
    ) and password[policy.min_occurrence - 1] != password[policy.max_occurrence - 1]


def solve_day2(
    day2_data: List[Tuple[PasswordPolicy, str]], validation_fcn: Callable
) -> int:
    """Counts the amount of passwords matching the policy."""

    validations = map(lambda case: validation_fcn(case[0], case[1]), day2_data)

    return sum(validations)


if __name__ == "__main__":
    converted_inputs = read_input(
        join(relpath(dirname(__file__)), "input.txt"), convert_line_of_input
    )

    print(
        f"Solution of Day 2 - Part 1 is "
        f"'{solve_day2(converted_inputs, validate_password_part1)}'"
    )
    print(
        f"Solution of Day 2 - Part 2 is "
        f"'{solve_day2(converted_inputs, validate_password_part2)}'"
    )
