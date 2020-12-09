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

--- Part Two ---

After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to
be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately
after the last instruction in the file. By changing exactly one jmp or nop, you can repair
the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction
infinite loop, never leaving that instruction. If you change almost any of the jmp instructions,
the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program
terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6

After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
"""
from os.path import dirname, relpath, join
from typing import List, Tuple
from common import read_input


instruction_type = Tuple[str, int]


class CommandExecutor:
    def __init__(self, commands: List[instruction_type]):

        self._commands = commands

        self._accumulator = 0
        self._lines_visited = []
        self._current_line = 0

    @property
    def accumulator(self):
        """Current value of the accumulator."""
        return self._accumulator

    def execute(self):
        """
        Executes the boot code until either the last line is reached or a line would be
        visited twice.
        """

        self.reset()

        while self._current_line < len(self._commands):
            self._execute_instruction(self._commands[self._current_line])

            if self._current_line in self._lines_visited:
                raise RecursionError(
                    f"Trying to executed line {self._current_line} twice."
                )

    def reset(self):
        """Resets the internal variables."""
        self._accumulator = 0
        self._lines_visited = []
        self._current_line = 0

    def _execute_instruction(self, instruction: instruction_type):
        """Executes a single instruction."""
        command_to_fcn = {
            "nop": self._no_operation,
            "acc": self._accumulate,
            "jmp": self._jump,
        }

        self._lines_visited.append(self._current_line)

        command_name, value = instruction
        command_to_fcn[command_name](value)

    def _no_operation(self, value: int):
        """Executes a 'nop' instruction."""
        self._current_line += 1

    def _accumulate(self, value: int):
        """Executes a 'acc' instruction."""
        self._current_line += 1
        self._accumulator += value

    def _jump(self, value: str):
        """Executes a 'jmp' instruction."""
        self._current_line += value


def input_converter(input_line: str) -> instruction_type:
    command, value = input_line.split()
    return command, int(value)


def solve_day8_part1(boot_code: List[instruction_type]):
    """
    Executes the boot code until either the last line is reached or a line would be
    visited twice.
    """

    command_executor = CommandExecutor(boot_code)
    try:
        command_executor.execute()
    except RecursionError:
        return command_executor.accumulator


def solve_day8_part2(boot_code: List[instruction_type]):
    """
    Creates local variants of the boot code by interchanging exactly one `jmp` and `nop` of
    each variant and then runs the code to check if it finished to execute the code without
    recursion.
    """

    for idx, instruction in enumerate(boot_code):
        command, value = instruction
        if command == "acc":
            continue

        boot_code_variant = boot_code[:]
        boot_code_variant[idx] = (
            "jmp" if command == "nop" else "nop",
            boot_code_variant[idx][1],
        )

        command_executor = CommandExecutor(boot_code_variant)
        try:
            command_executor.execute()
        except RecursionError:
            continue

        print(f"Found a bug in instruction No. {idx + 1}")
        return command_executor.accumulator

    raise RuntimeError("No bug fix found!")


if __name__ == "__main__":
    boot_code = read_input(
        join(relpath(dirname(__file__)), "input.txt"), input_converter
    )

    print(f"Solution of Day 1 - Part 1 is '{solve_day8_part1(boot_code)}'")
    print(f"Solution of Day 1 - Part 2 is '{solve_day8_part2(boot_code)}'")
