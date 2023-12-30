from pathlib import Path
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
            if part_two:
                seeds = [range(i, i+j) for i, j in zip(seeds[::2], seeds[1::2])]
        elif "map:" in line:
            source_category = line[0]
            almanac_data["maps"][source_category] = []
        elif source_category and len(line) > 1:
            numbers = list(map(int, line))
            number_ranges = (range(numbers[0], numbers[0]+numbers[2]), (range(numbers[1], numbers[1]+numbers[2])))
            almanac_data["maps"][source_category].append(number_ranges)
    
    if not part_two:
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

    if part_two:
        humidity_to_location_ranges = sorted(almanac_data["maps"]["humidity-to-location"], key=lambda x: x[0].start)
      
        for location_number in range(0, 9999999999999999999999):
            ranges_to_check = []
            for humidity_to_location_range_pair in humidity_to_location_ranges:
                if location_number in humidity_to_location_range_pair[0]:
                    ranges_to_check.append(humidity_to_location_range_pair)

            humidities = []
            if ranges_to_check:
                for range_check in ranges_to_check:
                    destination_idx = range_check[0].index(location_number)
                    source_number = range_check[1][destination_idx]
                    humidities.append(source_number)
            else:
                humidities.append(location_number)
            
            lowest_location = None
            for source_number in humidities:
                for source_category, map_ranges in reversed(almanac_data["maps"].items()):
                    if not source_category == "humidity-to-location":
                        for range_pair in map_ranges:
                            try:
                                if source_number in range_pair[0]:
                                    destination_idx = range_pair[0].index(source_number)
                                    source_number = range_pair[1][destination_idx]
                                    break
                            except:
                                pass
                    if source_category == "seed-to-soil":
                        for seed_range in seeds:
                            if source_number in seed_range:
                                if not lowest_location or lowest_location > location_number:
                                    lowest_location = location_number
                                    return lowest_location
        
    return lowest_location


if __name__ == "__main__":
    input = get_input()
    
    part_one_start_time = time.time()
    part_one = do_it(input)
    part_one_end_time = time.time()

    part_two_start_time = time.time()
    part_two = do_it(input, part_two=True)
    part_two_end_time = time.time()

    print("\nPart 1:", part_one, "\nElapsed Time: ", part_one_end_time - part_one_start_time)
    print("\nPart 2:", part_two, "\nElapsed Time: ", part_two_end_time - part_two_start_time)
