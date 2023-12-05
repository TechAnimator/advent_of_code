from pathlib import Path
import re


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(input):
    """

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:

    """
    for line in input:
        if line == input[1]:
            numbers_pattern = re.finditer(r'\d+', line) # Find all instances of numbers in the line
            symbols_pattern = re.finditer(r'[^.|^\d]+', line) # Find anything that isn't a number or a period in the line
            
            number_key = dict()
            for idx, number in enumerate(numbers_pattern):
                number_key[idx] = [number.start() - 1, number.end() + 1]
            print(number_key)
            print()
            for symbol in symbols_pattern:
                print(symbol.group(), symbol.start())
            print()


if __name__ == "__main__":
    input = get_input()
    print("Part 1:", do_it(input))
    # print("Part 2:", do_it(input))
