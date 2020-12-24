from copy import copy
from os.path import join, relpath, dirname
from typing import List, Tuple, Dict, Iterable, Union
from common import read_input


convert_output = List[Tuple[int, int, int]]

direction_to_moves = {
    "ne": (1, 0, -1),
    "e": (1, -1, 0),
    "se": (0, -1, 1),
    "nw": (0, 1, -1),
    "sw": (-1, 0, 1),
    "w": (-1, 1, 0),
}


def input_converter(input_line: str) -> convert_output:

    moves = []
    while len(input_line) > 0:
        try:
            moves.append(direction_to_moves[input_line[:1]])
            input_line = input_line[1:]
        except KeyError:
            moves.append(direction_to_moves[input_line[:2]])
            input_line = input_line[2:]

    return moves


def execute_moves(moves: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:

    position = (0, 0, 0)
    for move in moves:
        position = tuple(position[dim] + move[dim] for dim in range(3))
    return position


class TileMap:
    def __init__(self):

        self._known_tiles: Dict[Tuple[int, int, int], bool] = {}

    @property
    def black_tiles(self) -> List[Tuple[int, int, int]]:
        return [
            tile_pos for tile_pos, is_black in self._known_tiles.items() if is_black
        ]

    @property
    def black_tile_count(self):
        return len(self.black_tiles)

    def __getitem__(self, item):
        """Get the status of a tile. True means black, false means white."""
        return self._known_tiles.get(tuple(item), False)

    def __copy__(self):
        new_tile_map = TileMap()
        new_tile_map._known_tiles = {
            pos: True for pos, status in self._known_tiles.items() if status
        }
        return new_tile_map

    def flip_tile(self, coordinate: Tuple[int, int, int]):
        self._known_tiles[coordinate] = not self[coordinate]

    def count_adjacent_black_tiles(self, coordinate: Tuple[int, int, int]) -> int:

        black_count = 0
        for adjacent_coordinate in get_adjacent_tiles(coordinate):
            black_count += int(self[adjacent_coordinate])
        return black_count


def get_adjacent_tiles(position: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:

    adjacent_tiles = []
    for rel_coordinate in direction_to_moves.values():
        adjacent_coordinate = (
            position[0] + rel_coordinate[0],
            position[1] + rel_coordinate[1],
            position[2] + rel_coordinate[2],
        )
        adjacent_tiles.append(adjacent_coordinate)
    return adjacent_tiles


def validate_position(position: Union[List[int], Tuple[int, int, int]]):
    return sum(position) == 0 and len(position) == 3


def get_tile_map(
    black_tiles_directions: List[convert_output],
) -> TileMap:

    tile_map = TileMap()
    for moves in black_tiles_directions:
        tile_pos = execute_moves(moves)
        tile_map.flip_tile(tile_pos)
    return tile_map


def solve_part1(converted_input: List[convert_output]):
    tile_map = get_tile_map(converted_input)

    return tile_map.black_tile_count


def solve_part2(converted_input: List[convert_output], days: int):

    tile_map = get_tile_map(converted_input)

    for day in range(days):
        tile_map = apply_day_flip(tile_map)

    return tile_map.black_tile_count


def apply_day_flip(tile_map: TileMap) -> TileMap:

    tiles_to_flip = []
    known_tiles = {}
    for tile_pos in tile_map.black_tiles:
        tiles_to_check = [tile_pos] + get_adjacent_tiles(tile_pos)
        for adjacent_tile in tiles_to_check:

            if adjacent_tile in known_tiles:
                continue
            known_tiles[adjacent_tile] = True

            adjacent_black_tiles_count = tile_map.count_adjacent_black_tiles(
                adjacent_tile
            )
            if tile_map[adjacent_tile]:
                if adjacent_black_tiles_count not in (1, 2):
                    tiles_to_flip.append(adjacent_tile)
            else:
                if adjacent_black_tiles_count == 2:
                    tiles_to_flip.append(adjacent_tile)

    next_day_map = copy(tile_map)
    for tile in tiles_to_flip:
        next_day_map.flip_tile(tile)

    return next_day_map


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2020/24 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2020/24 - Part 2 is '{solve_part2(raw_input, 100)}'")
