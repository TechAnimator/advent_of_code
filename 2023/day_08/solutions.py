from pathlib import Path
import re


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(input, part_two=False):
    """Method for both parts one and two. Part one solves the puzzle using number values as given, part two accounts for Jacks as Jokers worth 1, not 11.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:
        int: Number of steps to get from AAA to ZZZ
    """
    number_of_steps = None

    steps = dict()
    for line in input:
        if "=" in line:
            step, left_right = line.split(" = ")
            left_right = re.findall(r'[A-Z]+', left_right)
            left_right = [code for code in left_right]
            steps[step] = left_right
        elif line:
            instructions = line
    
    current_step = steps["AAA"]

    step_count = 0
    not_zzz = True    
    while not_zzz:
        for direction in instructions:
            if direction == "L":
                current_key = current_step[0]
            else:
                current_key = current_step[1]
            current_step = steps[current_key]
            step_count += 1

            if current_key == "ZZZ":
                not_zzz = False
                break
        
    return step_count


if __name__ == "__main__":
    input = get_input()

    part_one = do_it(input)
    # part_two = do_it(input, part_two=True)

    print("\nPart 1:", part_one)
    # print("\nPart 2:", part_two)
