"""
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll
even have time to grab some food: all flights are currently delayed due to issues in luggage
processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about
bags and their contents; bags must be color-coded and must contain specific quantities of
other color-coded bags. Apparently, nobody responsible for these regulations considered how
long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue
bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black),
and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many
different bag colors would be valid for the outermost bag? (In other words: how many colors
can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could
then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could
then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one
shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules
is quite long; make sure you get all of it.)
"""

from typing import List, Tuple
from common import read_input

bag_registry = {}


class Bag:
    def __init__(self, color: str, containing_bags: List[Tuple[int, str]]):
        self.color = color
        self.containing_bags = containing_bags

        if self.color not in bag_registry:
            bag_registry[self.color] = self

    def __eq__(self, other):
        if isinstance(other, Bag):
            return self.color == other.color
        return False

    def __ne__(self, other):
        if isinstance(other, Bag):
            return self.color != other.color
        return True

    def __repr__(self):
        return f"{self.color.title()} {self.__class__.__name__}"

    def contains(self, bag: "Bag") -> bool:
        """Tests if this bag may contain a specified bag."""

        for sub_bag_specifier in self.containing_bags:
            sub_bag = bag_registry[sub_bag_specifier[1]]
            if sub_bag == bag:
                return True
            if sub_bag.contains(bag):
                return True
        return False


def input_converter(input: str) -> Bag:

    # get rid of the trailing dot
    input = input.rstrip(".")
    outer_bag, inner_bags_specifier = input.split("contain")
    inner_bags_specifier = inner_bags_specifier.split(', ')

    *outer_colors, _ = outer_bag.split()
    outer_color = " ".join(outer_colors)

    if inner_bags_specifier[0].strip() == "no other bags":
        return Bag(outer_color, [])

    inner_bags = []
    for inner_bag in inner_bags_specifier:
        count, *inner_colors, _ = inner_bag.split()
        inner_bags.append((int(count), " ".join(inner_colors)))

    bag = Bag(outer_color, inner_bags)

    return bag


def solve_day7_part1(converted_input: List[Bag]):

    my_bag = Bag("shiny gold", [])

    containing_count = 0
    for bag in bag_registry.values():
        if bag.contains(my_bag):
            containing_count += 1

    return containing_count


def solve_day7_part2(converted_input: List[Bag]):
    pass


if __name__ == "__main__":
    raw_input = read_input("inputs/day7.txt", input_converter)
    
    print(f"Solution of Day 1 - Part 1 is '{solve_day7_part1(raw_input)}'")
    print(f"Solution of Day 1 - Part 2 is '{solve_day7_part2(raw_input)}'")

