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

    if part_two:
        humidity_to_location_ranges = sorted(almanac_data["maps"]["humidity-to-location"], key=lambda x: x[0].start)
        # print(humidity_to_location_ranges)
        lowest_location = 999999999999999999999999999
        for hum_to_loc_ranges in humidity_to_location_ranges:
            print(hum_to_loc_ranges)
            for location in range(hum_to_loc_ranges[0].start, hum_to_loc_ranges[0].stop-1):
                # tracking_dict = dict()
                tracking_list = []
                
                idx = hum_to_loc_ranges[0].index(location)
                humidity = hum_to_loc_ranges[1][idx]
                tracking_list.append(location)
                tracking_list.append(humidity)
                source_number = humidity
                
                for source_category, map_ranges in reversed(almanac_data["maps"].items()):
                    if not source_category == "humidity-to-location":
                        for range_pair in map_ranges:
                            try:
                                destination_idx = range_pair[0].index(source_number)
                                source_number = range_pair[1][destination_idx]
                                break
                            except:
                                pass
                        tracking_list.append(source_number)

                print(tracking_list)

                if lowest_location > source_number:
                    lowest_location = source_number
                    # print(source_category, source_number, range_pair, location)

            print()


        # for potential_seed_number in range(0, 9999999999999999999999999999999):
        #     dest_number = potential_seed_number
            
        #     for source_category, map_ranges in reversed(almanac_data["maps"].items()):
                
        #         if source_category == "humidity-to-location":
        #             map_ranges = sorted(map_ranges, key=lambda x: x[1][0])
                
        #         source_number = dest_number
        #         for range_pair in map_ranges:
        #             if dest_number in range_pair[0]:                    
        #                 idx = range_pair[0].index(dest_number)
        #                 dest_number = range_pair[1][idx]
        #                 break
                
        #         if source_category == "humidity-to-location":
        #             if dest_number == potential_seed_number:
        #                 break
                

        #         print(source_category, source_number, dest_number, range_pair)

        #     # stored_location_numbers.append(dest_number)
        #     if dest_number in seeds and source_category == "seed-to-soil":
        #         return dest_number

        #     print()
                        

        # humidity_to_location_ranges = sorted(almanac_data["maps"]["humidity-to-location"], key=lambda x: x[1][0])

        # for h_to_l_range in humidity_to_location_ranges:
        #     for range_to_check in h_to_l_range:
        #         for number_check in range_to_check:
        #             dest_number = number_check
        #             for source_category, ranges in reversed(almanac_data["maps"].items()):
        #                 if not source_category.endswith("location"):
        #                     for sub_range_pair in ranges:
        #                         if dest_number in sub_range_pair[1]:
        #                             idx = sub_range_pair[1].index(dest_number)
        #                             new_dest_number = sub_range_pair[0][idx]
        #                             # print(idx, dest_number, new_dest_number, sub_range_pair)
        #                             dest_number = new_dest_number
        #                             break
                            
        #                     if source_category == "seed-to-soil":
        #                         print(source_category, dest_number)

                                    
            # break
        # sorted_ranges = ranges
        # sorted_ranges.sort(key=sorted_ranges[0][0].start)
        # print(ranges[0][0].start)
        # sorted(sorted_ranges, key=lambda x: idx, x in enumerate(x) if sorted_ranges[0][0].start < x[0idx][0].start)
        # sorted_ranges = []

        # for idx, num_range in enumerate(ranges):
        #     if not sorted_ranges:
        #         sorted_ranges.append(num_range)
        #     else:
        #         for ran in sorted_ranges:
        #             if 
        # ranges_to_check = None
        # for num_range in ranges:
        #     if not ranges_to_check:
        #         ranges_to_check = num_range
        #     elif num_range[0].start < ranges_to_check[0].start:
        #         ranges_to_check = num_range
                
        # print(ranges_to_check)
        # print(source_category)


        
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
