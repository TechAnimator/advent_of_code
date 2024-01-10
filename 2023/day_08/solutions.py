from pathlib import Path
import re
import math

def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(input, part_two=False):
    """Method for both parts one and two. The difference is searching for the element ZZZ vs elements all ending in Z and going through 1 node at a time
    vs simultaneously going through multiple nodes.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.
        part_two (bool): True if solving part two. False if solving part one.

    Returns:
        int: Number of steps to get from AAA to ZZZ
    """
    steps = dict()
    for line in input:
        # Store elements in a dict, key is the element itself and value is 2 elements for left/right based on instruction
        if "=" in line:
            step, left_right = line.split(" = ")
            left_right = re.findall(r'[A-Z]+', left_right)
            left_right = [code for code in left_right]
            steps[step] = left_right
        elif line:
            instructions = line # Left/Right instructions

    # Part two looks for elements that end in Z while part 1 looks for the element that is exactly ZZZ
    # Part two uses multiple elements while part 1 only starts with AAA
    if part_two:
        key_to_search_for = "Z"
        first_steps = [directions for step, directions in steps.items() if step.endswith("A")]
    else:
        key_to_search_for = "ZZZ"
        first_steps = [steps["AAA"]]

    # Store the number of steps necessary to find the end key (elements ending in Z for part 2, or ZZZ for part 1)
    steps_to_z = []
    for current_left_right in first_steps:
        step_count = 0
        element_is_not_goal = True # Set this to true since the first element isn't our goal
        while element_is_not_goal: # Keep going until the element we need is found
            # Go through the left/right instructions, counting steps for each iteration
            for direction in instructions:
                if direction == "L":
                    current_key = current_left_right[0]
                else:
                    current_key = current_left_right[1]
                current_left_right = steps[current_key]
                step_count += 1

                # When the element that is equal to Z (part 1) or ending in Z (part 2) is found, break the loop and set the bool to False
                if current_key.endswith(key_to_search_for):
                    element_is_not_goal = False

        steps_to_z.append(step_count) # Add the step count to the list we will find the lowest common multiple from

    return math.lcm(*steps_to_z) # Get the lowest common multiple from all the step counts (part 1 will just have a single step count)
    

if __name__ == "__main__":
    input = get_input()

    part_one = do_it(input)
    part_two = do_it(input, part_two=True)

    print("\nPart 1:", part_one)
    print("\nPart 2:", part_two)
