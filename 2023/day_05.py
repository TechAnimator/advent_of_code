from pathlib import Path
import itertools
import time


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(input):
    """Organizes all seed and map data, then passes that data through the solvers for both parts.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:
        int: Answer to Part 1.
        int: Answer to Part 2.
    """
    almanac_data = dict()
    source_category = None
    for line in input:
        line = line.split(" ")
        if "seeds:" in line:
            seeds = list(map(int, line[1:]))
        elif "map:" in line:
            source_category = line[0]
            almanac_data[source_category] = list()
        elif source_category and len(line) > 1:
            numbers = list(map(int, line))
            number_ranges = (range(numbers[0], numbers[0]+numbers[2]), (range(numbers[1], numbers[1]+numbers[2])))
            almanac_data[source_category].append(number_ranges)

    return part_one(almanac_data, seeds), part_two(almanac_data, seeds)


def part_one(almanac_data, seeds):
    """Goes through all seeds and runs them through the maps to find the lowest location generated by the maps.

    Args:
        almanac_data (dict): Map data from input sorted by category. Data is stored as ranges.
        seeds (list of int): Seed data from input sorted into a list of integers.

    Returns:
        int: Lowest location found from passing all seeds through the data.
    """
    lowest_location = None
    for seed_number in seeds:
        for _, ranges in almanac_data.items():
            for range_pair in ranges:
                dest_range = range_pair[0]
                source_range = range_pair[1]
                if seed_number in source_range:
                    idx = source_range.index(seed_number)
                    seed_number = dest_range[idx]
                    break
                
        if not lowest_location or (seed_number < lowest_location):
            lowest_location = seed_number
    
    return lowest_location


def part_two(almanac_data, seeds):
    """
    Looks for seeds in reverse, by starting at 0 and going through the maps starting at "humidity-to-location" until the final converted
    number in "seed-to-soil" corresponds with a number found in seed.

    Args:
        almanac_data (dict): Map data from input sorted by category. Data is stored as ranges.
        seeds (list of int): Seed data from input sorted into a list of integers.

    Returns:
        int: Lowest location found from passing possible locations starting at 0 through the data in reverse.
    """
    # Organize list of seeds as ranges, every second (odd index) number is how long the range should be based off the first (even index) number
    seeds = [range(i, i+j) for i, j in zip(seeds[::2], seeds[1::2])]

    # Sort the humidity-to-location ranges in order of lowest location first to save time from iterating through unnecessary rangess
    humidity_to_location_ranges = sorted(almanac_data["humidity-to-location"], key=lambda x: x[0].start)
    del almanac_data["humidity-to-location"] # Remove from the dict now that the data is stored elsewhere

    # Iterate through an infinite count until the lowest location is found and returned
    for location_number in itertools.count(start=0):
        ranges_to_check = list() # Create list to store rages in for checking
        for humidity_to_location_range_pair in humidity_to_location_ranges:
            if location_number in humidity_to_location_range_pair[0]:
                # If the current number is found in the destination range of a pair, store the range pair for checking
                ranges_to_check.append(humidity_to_location_range_pair)

        # Check if location number is in any of the destination ranges and convert it if so. If not, store the location number as is.
        humidities = list()
        if ranges_to_check:
            for range_check in ranges_to_check:
                destination_idx = range_check[0].index(location_number)
                source_number = range_check[1][destination_idx]
                humidities.append(source_number)
        else:
            humidities.append(location_number)
        
        # Check all numbers that are in the humidities list, if the final result from "seed-to-soil" is found in seeds, return as the answer.
        for source_number in humidities:
            for _, map_ranges in reversed(almanac_data.items()):
                for range_pair in map_ranges:
                    if source_number in range_pair[0]:
                        destination_idx = range_pair[0].index(source_number)
                        source_number = range_pair[1][destination_idx]
                        break
            for seed_range in seeds:
                if source_number in seed_range:
                    return location_number


if __name__ == "__main__":
    input = get_input()

    start_time = time.time()
    part_one, part_two = do_it(input)
    end_time = time.time()

    print("\nPart 1:", part_one)
    print("\nPart 2:", part_two)

    print("\nElapsed Time: ", end_time - start_time)