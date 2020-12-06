"""
--- Day 3: Toboggan Trajectory ---

With the toboggan login problems resolved, you set off toward the airport. While travel by
toboggan might be easy, it's certainly not safe: there's very minimal steering and the area
is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid.
You make a map (your puzzle input) of the open squares (.) and trees (#) you can see.
For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once involving arboreal
genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

You start on the open square (.) in the top-left corner and need to reach the bottom (below
the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers
rational numbers); start by counting all the trees you would encounter for the slope
right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1.
Then, check the position that is right 3 and down 1 from there, and so on until you go past
the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open
square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1,
how many trees would you encounter?

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden
arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes,
you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively;
multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the
listed slopes?

"""
from typing import List, Tuple

from common import read_input


def convert_tree_map(tree_map_string: str) -> List[bool]:
    """Converts one line of the tree map into an list of logical with true values at
    very place of the map where a tree would be."""

    return [True if char == "#" else False for char in tree_map_string]


def count_on_slope(tree_map: List[List[bool]], slope: Tuple[int, int]) -> int:
    """Counts the number of tree encountered when running the tobogan with a defined slope."""

    tree_count = 0
    current_position = [0, 0]
    map_row_cnt = len(tree_map)
    map_col_cnt = len(tree_map[0])
    while current_position[0] < map_row_cnt:
        tree_count += int(tree_map[current_position[0]][current_position[1]])

        current_position[0] += slope[0]
        current_position[1] = (current_position[1] + slope[1]) % map_col_cnt

    return tree_count


if __name__ == "__main__":

    input_data = read_input("./inputs/day3.txt", convert_tree_map)

    # first entry steps down, second entry steps to the right
    slope = (1, 3)

    print(f"Solution of Day 3 - Part 1 is " f"'{count_on_slope(input_data, slope)}'")

    # part 2
    prod_of_encountered_trees = 1
    for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        prod_of_encountered_trees *= count_on_slope(input_data, slope)

    print(f"Solution of Day 3 - Part 2 is " f"'{prod_of_encountered_trees}'")
