from pathlib import Path
import re
import datetime
import time


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(input, part_two=False):
    """

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:
    """
    almanac_data = {"seeds": None, "maps": {}}
    source_category = None
    for line in input:
        line = line.split(" ")
        if "seeds:" in line:
            seeds = list(map(int, line[1:]))
        elif "map:" in line:
            source_category = line[0]
            almanac_data["maps"][source_category] = []
        elif source_category and len(line) > 1:
            numbers = list(map(int, line))
            number_ranges = (range(numbers[0], numbers[0]+numbers[2]+1), (range(numbers[1], numbers[1]+numbers[2]+1)))
            almanac_data["maps"][source_category].append(number_ranges)
    
    lowest_location = None
    for seed_number in seeds:
        for source_category, ranges in almanac_data["maps"].items():
            for num_range in ranges:
                dest_range = num_range[0]
                source_range = num_range[1]
                if seed_number in source_range:
                    idx = source_range.index(seed_number)
                    seed_number = dest_range[idx]
                    break
                
        if not lowest_location or (seed_number < lowest_location):
            lowest_location = seed_number
        
    return lowest_location


if __name__ == "__main__":
    input = get_input()
    
    part_one_start_time = time.time()
    part_one = do_it(input)
    part_one_end_time = time.time()

    part_two_start_time = time.time()
    part_two = do_it(input, part_two=False)
    part_two_end_time = time.time()

    print("\nPart 1:", part_one, "\nElapsed Time: ", part_one_end_time - part_one_start_time)
    print("\nPart 2:", part_two, "\nElapsed Time: ", part_two_end_time - part_two_start_time)
