"""
--- Day 6: Custom Customs ---

As your flight approaches the regional airport where you'll switch to a much larger plane,
customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is
identify the questions for which anyone in your group answers "yes". Since your group is just
you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and
asks if you can help. For each of the people in their group, you write down the questions
for which they answer "yes", one per line. For example:

abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z.
(Duplicate answers to the same question don't count extra; each question counts at most
once.)

Another group asks for your help, then another, and eventually you've collected answers
from every group on the plane (your puzzle input). Each group's answers are separated by
a blank line, and within each group, each person's answers are on a single line.
For example:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes".
What is the sum of those counts?

--- Part Two ---

As you finish the last group's customs declaration, you notice that you misread one word
in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify
the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not
answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is
the sum of those counts?
"""
from os.path import join, relpath, dirname
from typing import List

from common import read_input_groups


def solve_day6_part1(groups_yes_answers: List[List[str]]) -> int:
    unique_groups_answers = [
        set("".join([answer for answer in group])) for group in groups_yes_answers
    ]

    return sum([len(unique_answers) for unique_answers in unique_groups_answers])


def solve_day6_part2(groups_yes_answers: List[List[str]]) -> int:

    matching_answers_per_group = []
    for answers_of_group in groups_yes_answers:
        unique_answers = set("".join([answer for answer in answers_of_group]))
        answers_counts = {answer: 0 for answer in unique_answers}

        for answers_of_person in answers_of_group:
            for answer in answers_of_person:
                answers_counts[answer] += 1

        matching_answers = sum(
            [
                1
                for answer_counts in answers_counts.values()
                if answer_counts == len(answers_of_group)
            ]
        )

        matching_answers_per_group.append(matching_answers)

    return sum(matching_answers_per_group)


if __name__ == "__main__":
    groups_yes_answers = read_input_groups(
        join(relpath(dirname(__file__)), "input.txt"), str
    )

    print(f"Solution of Day 6 - Part 1 is " f"'{solve_day6_part1(groups_yes_answers)}'")
    print(f"Solution of Day 6 - Part 2 is " f"'{solve_day6_part2(groups_yes_answers)}'")
