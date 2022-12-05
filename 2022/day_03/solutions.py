from pathlib import Path
import string


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    rounds = [round for round in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]

    return rounds


def get_common_item_single(line):
    """Finds the common "item" (character) that exists in both halves of a given string.

    Args:
        line (str): Line of random upper and lower case characters.
    """
    # Split the line down the middle and find the common item/letter between the two halves
    line_length = len(line)
    compartment_one = line[slice(0, line_length // 2)]
    compartment_two = line[slice(line_length // 2, line_length)]
    common_item = "".join(set(compartment_one).intersection(compartment_two))

    return common_item


def get_common_item_group(lines):
    """Finds the common "item" (character) that exists in a group of a given number of strings.

    Args:
        lines (list of str): List of lines of random upper and lower case characters.
    """
    # Start by finding the common items/letters in the first two lines, continue to filters through the rest of the lines
    common_items = "".join(set(lines[0]).intersection(lines[1]))
    common_item = next("".join(set(common_items).intersection(line)) for line in lines[2:])

    return common_item


def generate_priority_dict():
    """Generates a dictionary where the keys are all letters of the alphabet, both lower and upper case.

    Returns:
        dict: {"a":1, "b":2, "c":3..."z":26, "A":27, "B":28, "C":29..."Z":52}
    """
    # Create the dictionary of letters and set values to 0
    alphabet_dict = dict.fromkeys(string.ascii_letters, 0)

    # Set values from 1 to 52 from a to Z (lower a is first: 1, upper Z is last: 52)
    for idx, letter in enumerate(alphabet_dict):
        alphabet_dict[letter] = idx + 1

    return alphabet_dict


def get_totals():
    """Gets total numbers from parts one and two of the puzzle.

    Returns:
        int: Total from single line of letters, int: Total from 3 lines of letters
    """
    rounds = get_input()
    item_priorities = generate_priority_dict()
    part_one_total = 0
    part_two_total = 0

    # Part One
    for round in rounds:
        common_item = get_common_item_single(round)
        part_one_total += item_priorities[common_item]

    # Part Two
    # Set group_size to 3, but this can be used to group together whatever the inputted amount is
    group_size = 3

    # This list comp will create a list of lists that include 3 strings per nested list
    # Ex: [[vJrwpWtwJgWr, jqHRNqRjqzjGDLGL, PmmdzqPrVv], [hcsFMMfFFhFp, LrsFMfFZSrLrFZsSL, PwwTWBwg]]
    list_of_groups = [rounds[idx : idx + group_size] for idx in range(0, len(rounds), group_size)]

    # Get the total number from each group of 3 and add to grand total
    for group in list_of_groups:
        common_item = get_common_item_group(group)
        part_two_total += item_priorities[common_item]

    return part_one_total, part_two_total


if __name__ == "__main__":
    part_one_total, part_two_total = get_totals()
    print("Part 1: {}".format(part_one_total))
    print("Part 2: {}".format(part_two_total))
