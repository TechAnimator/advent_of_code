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
    point_total_all = 0

    for line in input:
        winning_numbers, my_numbers = line.split(":")[1].split("|")
        winning_numbers = [int(num) for num in re.findall(r'\d+', winning_numbers)]
        my_numbers = [int(num) for num in re.findall(r'\d+', my_numbers)]
        matches = set(winning_numbers).intersection(my_numbers)
        number_of_matches = len(matches)
        
        if number_of_matches:
            point_total_card = 1
            for match_number in range(2, number_of_matches+1):
                point_total_card *= 2
            point_total_all += point_total_card

    return point_total_all


if __name__ == "__main__":
    input = get_input()
    part_one = do_it(input)
    print("Part 1:", part_one)
    # print("Part 2:", part_two)
