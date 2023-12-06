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
    stored_data = dict()
    for line_idx, line in enumerate(input):
        numbers_pattern = re.finditer(r'\d+', line) # Find all instances of numbers in the line
        symbols_pattern = re.finditer(r'[^.|^\d]+', line) # Find anything that isn't a number or a period in the line

        number_key = dict()
        symbol_locations = list()
        for idx, number in enumerate(numbers_pattern):
            # Store every instance of a number in it's own embedded dict with the number and the range it appears.
            # Expand the range by 1 on each side to account for diagonal symbols when comparing lines.
            number_key[idx] = {"number": int(number.group()), "range": [number.start() - 1, number.end() + 1]}

        for symbol in symbols_pattern:
            symbol_locations.append(symbol.start())

        stored_data[line_idx] = {"numbers": number_key, "symbols": symbol_locations}

    data_length = len(stored_data)
    total = 0
    for line_number in range(data_length):
        if line_number != 0:
            last_line = stored_data[line_number-1]
        else:
            last_line = {"symbols": list()}

        if line_number != data_length-1:
            next_line = stored_data[line_number+1]
        else:
            next_line = {"symbols": list()}
        current_line = stored_data[line_number]

        all_symbols = list()
        all_symbols.extend(last_line["symbols"])
        all_symbols.extend(current_line["symbols"])
        all_symbols.extend(next_line["symbols"])
        all_symbols.sort()

        for idx, data in current_line["numbers"].items():
            next_to_symbol = any(data["range"][0] <= x < data["range"][1] for x in all_symbols)
            if next_to_symbol:
                total += data["number"]

    return total


if __name__ == "__main__":
    input = get_input()
    print("Part 1:", do_it(input))
    # print("Part 2:", do_it(input))
