from pathlib import Path
import re


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(input):
    """Part 1.
    Parse all lines to store numbers and symbols first to store all information.
    Go through stored data to cross check lines with each other to find all the numbers that are next to a symbol.
    Line by line, add any applicable numbers to the total that gets returned at the end of the process.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:
        int: Total of all the numbers that are next to a symbol.
    """
    stored_data = dict()
    for line_idx, line in enumerate(input):
        numbers_pattern = re.finditer(r'\d+', line) # Find all instances of numbers in the line
        symbols_pattern = re.finditer(r'[^.|^\d]+', line) # Find anything that isn't a number or a period in the line

        number_key = dict()
        symbol_locations = list()
        for idx, number in enumerate(numbers_pattern):
            # Store every instance of a number in its own unique embedded dict with the number and the range it appears.
            # Expand the range by 1 on each side to account for diagonal symbols when comparing lines.
            number_key[idx] = {"number": int(number.group()), "range": [number.start() - 1, number.end() + 1]}

        # Store the indicies for all symbols (we don't care what the symbols are, just where they are)
        for symbol in symbols_pattern:
            symbol_locations.append(symbol.start())

        # Store the number dict and symbol list for the line
        stored_data[line_idx] = {"numbers": number_key, "symbols": symbol_locations}

    # Get the number of lines to loop through and create the total variable to add up the numbers applicable to the puzzle prompt
    data_length = len(stored_data)
    total = 0

    for line_number in range(data_length):
        all_symbols = list()

        if line_number != 0: # Add the symbol locations from the previous line for the 2nd line and beyond
            all_symbols.extend(stored_data[line_number-1]["symbols"])
        if line_number != data_length - 1: # Add the symbol locations from the next line up until the last line
            all_symbols.extend(stored_data[line_number+1]["symbols"])
        all_symbols.extend(stored_data[line_number]["symbols"]) # Add the symbols locations from the current line

        all_symbols.sort() # Unnecessary but I like a sorted list of numbers

        # Go through all the numbers in the current line and cross check with the symbols from the previous, current, and next
        # lines to see what numbers are applicable to the puzzle prompt and next to a symbol
        for idx, data in stored_data[line_number]["numbers"].items():
            next_to_symbol = any(data["range"][0] <= x < data["range"][1] for x in all_symbols)
            if next_to_symbol:
                total += data["number"]

    return total


if __name__ == "__main__":
    input = get_input()
    print("Part 1:", do_it(input))
    # print("Part 2:", do_it(input))
