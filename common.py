from typing import List, Callable, Any


def read_lines_of_file(file: str) -> List[str]:
    """Reads all lines from a file and returns a list of the lines."""

    with open(file, "r") as r:
        input_data = r.read()

    return input_data.splitlines(keepends=False)


def read_input(file: str, line_converter: Callable) -> List[Any]:
    """Reads the input of the file and converts it with the specified converter."""

    return list(map(line_converter, read_lines_of_file(file)))
