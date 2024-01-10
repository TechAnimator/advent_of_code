from pathlib import Path
import re
import math

def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(input, part_two=False):
    """Method for both parts one and two.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.
        part_two (bool): True if solving part two. False if solving part one.

    Returns:
        int: 
    """
    for line in input:
        history_of_value = list(map(int, line.split()))

        difference_sequences = list()


if __name__ == "__main__":
    input = get_input()

    part_one = do_it(input)
    part_two = do_it(input, part_two=True)

    print("\nPart 1:", part_one)
    print("\nPart 2:", part_two)
