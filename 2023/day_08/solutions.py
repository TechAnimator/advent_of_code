from pathlib import Path
import re
import math

def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(input):
    """Method for both parts one and two. Part one solves the puzzle using number values as given, part two accounts for Jacks as Jokers worth 1, not 11.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:
        int: Number of steps to get from AAA to ZZZ
    """
    steps = dict()
    for line in input:
        if "=" in line:
            step, left_right = line.split(" = ")
            left_right = re.findall(r'[A-Z]+', left_right)
            left_right = [code for code in left_right]
            steps[step] = left_right
        elif line:
            instructions = line

    return part_one(instructions, steps), part_two(instructions, steps)


def part_one(instructions, steps):
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

    return step_count


def part_two(instructions, steps):
    first_steps = [directions for step, directions in steps.items() if step.endswith("A")]

    steps_to_z = []
    for step in first_steps:
        step_count = 0
        not_zzz = True  
        while not_zzz:
            for direction in instructions:
                if direction == "L":
                    current_key = step[0]
                else:
                    current_key = step[1]
                step = steps[current_key]
                step_count += 1
            if current_key.endswith("Z"):
                not_zzz = False
        steps_to_z.append(step_count)

    return math.lcm(*steps_to_z)
    

if __name__ == "__main__":
    input = get_input()

    part_one, part_two = do_it(input)

    print("\nPart 1:", part_one)
    print("\nPart 2:", part_two)
