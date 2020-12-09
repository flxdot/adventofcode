from os.path import join, relpath, dirname
from typing import List, Tuple
from common import read_input


convert_output = int


class XmasEncryptionExploit:
    def __init__(self, preamble_length: int = 25):

        self.preamble_length = preamble_length

    def exploit(self, full_data: List[int]) -> int:
        """Returns the index of the first non matching checksum value of the given xmax
        encrypted data"""

        for value, checksum in XmasEncryptedData(full_data, self.preamble_length):
            if self._data_package_is_weak(value, checksum):
                return value

    def get_weakness(self, full_data: List[int]) -> List[int]:
        """Returns sequence of numbers of weakness."""

        exploit_value = self.exploit(full_data)

        data_len = len(full_data)
        for start_index in range(data_len):
            for end_index in range(start_index, data_len):
                cur_data = full_data[start_index:end_index]
                range_sum = sum(cur_data)
                if range_sum == exploit_value:
                    return cur_data
                if range_sum > exploit_value:
                    break
        raise ValueError("No exploit found")

    @staticmethod
    def _data_package_is_weak(value: int, checksum: List[int]) -> bool:

        choices = {val: val for val in checksum}

        for val in checksum:
            if value - val in choices:
                return False
        return True


class XmasEncryptedData:
    def __init__(self, data: List[int], preamble_length: int):

        self.data = data
        self.preamble_length = preamble_length

        self._current_index = 0

    def __iter__(self):
        self._current_index = 0
        return self

    def __next__(self) -> Tuple[int, List[int]]:
        idx = self._current_index
        data_idx = idx + self.preamble_length
        if data_idx > len(self.data):
            raise StopIteration
        self._current_index += 1
        return (
            self.data[idx + self.preamble_length],
            self.data[idx : idx + self.preamble_length],
        )


def input_converter(input_line: str) -> convert_output:
    return int(input_line)


def solve_part1(converted_input: List[convert_output]):
    weakness_values = get_first_xmax_weakness(converted_input)
    return


def get_first_xmax_weakness(
    encrypted_data: List[convert_output], preamble_length: int = 25
) -> int:
    """Returns the index of the first non matching checksum value of the given xmax
    encrypted data"""

    return XmasEncryptionExploit(preamble_length).exploit(encrypted_data)


def get_encrypted_xmas_weakness(
    encrypted_data: List[convert_output], preamble_length: int = 25
) -> int:
    """Returns the index of the first non matching checksum value of the given xmax
    encrypted data"""

    weakness_values = XmasEncryptionExploit(preamble_length).get_weakness(
        encrypted_data
    )
    return min(weakness_values) + max(weakness_values)


def solve_part2(converted_input: List[convert_output]):
    return get_encrypted_xmas_weakness(converted_input)


if __name__ == "__main__":
    raw_input = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of 2020/9 - Part 1 is '{solve_part1(raw_input)}'")
    print(f"Solution of 2020/9 - Part 2 is '{solve_part2(raw_input)}'")
