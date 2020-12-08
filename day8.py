"""
--- Day 8: Handheld Halting ---

Your flight to the major airline hub reaches cruising altitude without incident. While
you consider checking the in-flight menu for one of those drinks that come with a little
umbrella, you are interrupted by the kid sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your puzzle input)
of the device. You should be able to fix it, but first you need to be able to run the code
in isolation.

The boot code is represented as a text file with one instruction per line of text. Each
instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number
like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given
in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator
starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found
using the argument as an offset from the jmp instruction; for example, jmp +2 would skip
the next instruction, jmp +1 would continue to the instruction immediately below it, and
jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is
executed next.
For example, consider the following program:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

These instructions are visited in this order:

nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |

First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1)
and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases
the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3.
It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.

This is an infinite loop: with this sequence of jumps, the program will run forever.
The moment the program tries to run any instruction a second time, you know it will
never terminate.

Immediately before the program would run an instruction a second time, the value in the
accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed a second
time, what value is in the accumulator?
"""

from typing import List, Tuple
from common import read_input


convert_output = Tuple[str, int]


class CommandExecutor:

    def __init__(self, commands: List[convert_output]):

        self._commands = commands

        self._accumulator = 0
        self._lines_visited = []
        self._current_line = 0

    def execute(self):

        self.reset()

        while self._current_line not in self._lines_visited:
            self._execute_line(self._commands[self._current_line])

        return self._accumulator

    def reset(self):
        self._accumulator = 0
        self._lines_visited = []
        self._current_line = 0

    def _execute_line(self, command: convert_output):

        command_to_fcn = {
            "nop": self._no_operation,
            "acc": self._accumulate,
            "jmp": self._jump
        }

        self._lines_visited.append(self._current_line)

        command_name, value = command
        command_to_fcn[command_name](value)

    def _no_operation(self, value: int):
        self._current_line += 1

    def _accumulate(self, value: int):
        self._current_line += 1
        self._accumulator += value

    def _jump(self, value: str):
        self._current_line += value


def input_converter(input_line: str) -> convert_output:
    command, value = input_line.split()
    return command, int(value)


def solve_day8_part1(converted_input: List[convert_output]):

    command_executor = CommandExecutor(converted_input)
    return command_executor.execute()


def solve_day8_part2(converted_input: List[convert_output]):
    pass


if __name__ == "__main__":
    raw_input = read_input("inputs/day8.txt", input_converter)

    print(f"Solution of Day 1 - Part 1 is '{solve_day8_part1(raw_input)}'")
    print(f"Solution of Day 1 - Part 2 is '{solve_day8_part2(raw_input)}'")
