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

--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but
because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus
2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this
example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""

from typing import List, Tuple, Dict
from common import read_input


bag_registry: Dict[str, "Bag"] = {}


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

    @property
    def number_of_containing_bags(self) -> int:
        """Counts the number of all containing bags."""

        bag_count = 0
        for sub_bag_count, sub_bag_color in self.containing_bags:
            bag_count += sub_bag_count
            bag_count += (
                sub_bag_count * bag_registry[sub_bag_color].number_of_containing_bags
            )
        return bag_count


def input_converter(input_line: str) -> Bag:

    # get rid of the trailing dot
    input_line = input_line.rstrip(".")
    outer_bag, inner_bags_specifier = input_line.split("contain")
    inner_bags_specifier = inner_bags_specifier.split(", ")

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

    my_bag = bag_registry["shiny gold"]

    containing_count = 0
    for bag in bag_registry.values():
        if bag.contains(my_bag):
            containing_count += 1

    return containing_count


def solve_day7_part2(converted_input: List[Bag]):

    my_bag = bag_registry["shiny gold"]

    return my_bag.number_of_containing_bags


if __name__ == "__main__":
    raw_input = read_input("inputs/day7.txt", input_converter)

    print(f"Solution of Day 1 - Part 1 is '{solve_day7_part1(raw_input)}'")
    print(f"Solution of Day 1 - Part 2 is '{solve_day7_part2(raw_input)}'")
