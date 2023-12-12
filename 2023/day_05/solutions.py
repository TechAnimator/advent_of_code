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

    all_ranges = dict()
    for key, value in almanac_data.items():
        if key == "maps":
            for map_type, sub_value in value.items():
                all_ranges[map_type] = list()
                for values in sub_value:
                    range_key = dict()
                    if values[0]:
                        for idx in range(int(values[2])):
                            range_key[int(values[1]) + idx] = int(values[0]) + idx
                        all_ranges[map_type].append(range_key)

    for seed in almanac_data["seeds"]:
        seed_number = int(seed)
        print("Start: ", seed_number)

        for map_type, ranges in all_ranges.items():
            for range_conversion in ranges:
                if seed_number in range_conversion:
                    seed_number = range_conversion[seed_number]
                    if map_type == "fertilizer-to-water":
                        print(range_conversion)
                        print(seed_number)
            print(map_type, seed_number)
        # for location_conversion in location_range_list:
        #     if seed_number in location_conversion:
        #         if seed_number < location_conversion[seed_number]:
        #             seed_number = location_conversion[seed_number]
        print("End: ", seed_number)
        print()

    return None, None


if __name__ == "__main__":
    input = get_input()
    part_one, part_two = do_it(input)
    print("Part 1:", part_one)
    print("Part 2:", part_two)
