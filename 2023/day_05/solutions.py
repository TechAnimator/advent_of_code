from pathlib import Path
import re


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

            # This code seems to work for the example data but it is very slow and needs a pass for speed for the actual input.
            # seeds = seeds
            # if part_two:
            #     seeds = [(i, j) for i, j in zip(seeds[::2], seeds[1::2])]
            #     new_seeds = []
            #     for pair in seeds:
            #         new_seeds.append(pair[0])
            #         new_seeds.extend(range(pair[0]+1, pair[0]+pair[1]))
            #     seeds = new_seeds

        elif "map:" in line:
            source_category = line[0]
            almanac_data["maps"][source_category] = []
        elif source_category and len(line) > 1:
            numbers = list(map(int, line))
            almanac_data["maps"][source_category].append((numbers[0], (numbers[1], numbers[1]+numbers[2])))
    
    lowest_location = None
    for seed_number in seeds:
        for source_category, data in almanac_data["maps"].items():
            for numbers in data:
                if seed_number in range(numbers[1][0], numbers[1][1]):
                    seed_number = (seed_number - numbers[1][0]) + numbers[0]
                    break
        if not lowest_location or (seed_number < lowest_location):
            lowest_location = seed_number
        
    return lowest_location


if __name__ == "__main__":
    input = get_input()
    part_one = do_it(input)
    part_two = do_it(input, part_two=True)
    print("Part 1:", part_one)
    print("Part 2:", part_two)
