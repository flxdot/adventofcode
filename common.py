import time
from contextlib import contextmanager
from typing import List, Callable, Any


def read_lines_of_file(file: str) -> List[str]:
    """Reads all lines from a file and returns a list of the lines."""

    with open(file, "r") as r:
        input_data = r.read()

    return input_data.splitlines(keepends=False)


def read_input(file: str, line_converter: Callable) -> List[Any]:
    """Reads the input of the file and converts it with the specified converter."""

    return list(map(line_converter, read_lines_of_file(file)))


def read_input_groups(file: str, line_converter: Callable) -> List[List[Any]]:
    """Reads the input of the file and converts each line with the specified converter.
    Additionally the lines will be grouped by empty lines."""

    groups = [[]]
    for line in read_input(file, str):
        if not line.strip():
            groups.append([])
            continue
        groups[-1].append(line_converter(line))

    return groups

@contextmanager
def time_it(name: str = None):
    """Context manager to measure how long the execution of a certain code fragment takes.
    The measured execution time will be printed into the console.

    One may specify a name for the test for better traceability by specifying the name input.
    """

    start_time = time.time()
    yield
    duration = time.time() - start_time

    if name is not None:
        print(f"Execution of {name} took {duration*1000}ms")
    else:
        print(f"Execution took {duration*1000}ms")
