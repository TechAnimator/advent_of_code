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
    almanac_data = {"seeds": None, "maps": {}}
    source_category = None
    for idx, line in enumerate(input):
        line = line.split(" ")
        if "seeds:" in line:
            almanac_data["seeds"] = line[1:]
        elif "map:" in line:
            source_category = line[0]
            almanac_data["maps"][source_category] = []
        elif source_category:
            almanac_data["maps"][source_category].append(line)

    for key, value in almanac_data.items():
        if key == "maps":
            for sub_key, sub_value in value.items():
                print(sub_key)

    return None, None


if __name__ == "__main__":
    input = get_input()
    part_one, part_two = do_it(input)
    print("Part 1:", part_one)
    print("Part 2:", part_two)
