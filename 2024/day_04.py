from pathlib import Path
import re


def get_input():
    '''Parse the input text file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    '''
    return [line for line in Path(__file__).parent.joinpath('day_04_input.txt').read_text().split('\n')]


def eight_way_lookup(letter):
    pass

def search_for_next(letter):
    pass


def do_it():
    '''Run both part 1 and 2 in the same call. Store the string of numbers from each line into a list.
    
    For part 1:
    
    For part 2:

    Returns:
        int, int: Nunmber of safe reports (part 1 answer), Number of new safe reports (part 2 answer)
    '''
    # Get input
    input = get_input()

    # Get lines vertically from input
    vertical_input_lines = zip(*input)

    # Get lines diagonally from input
    # diagonal_input_lines = zip(*input)
    
    # Regex compile to search for XMAS spelled both forward and backward
    regex_find_xmas_forward = re.compile("XMAS")
    regex_find_xmas_backward = re.compile("SAMX")

    # Count variable to add instance counts to
    xmas_count = 0

    # Iterate through all horizontal lines for XMAS instances and add to the count
    for line in input:
        xmas_forward = re.findall(regex_find_xmas_forward, line)
        xmas_backward = re.findall(regex_find_xmas_backward, line)

        xmas_count += (len(xmas_forward) + len(xmas_backward))
    
    # Iterate through all vertical lines for XMAS instances and add to the count
    for line in vertical_input_lines:
        line = "".join(tuple(line))

        xmas_downward = re.findall(regex_find_xmas_forward, line)
        xmas_upward = re.findall(regex_find_xmas_backward, line)

        xmas_count += (len(xmas_downward) + len(xmas_upward))

    # Iterate through all diagonal lines for XMAS instances and add to the count
    # TODO

    return xmas_count, None


if __name__ == '__main__':
    part_one, part_two = do_it()
    print("Part 1:", part_one)
    print("Part 2:", part_two)
