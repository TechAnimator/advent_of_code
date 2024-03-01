from pathlib import Path


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    # Split input into a list of lines
    lines = [
        line
        for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")
    ]
    return lines


def organize_stacks():
    """Sorts the stacks from the input as nested lists into a main organized list.
    
    Returns:
        list of lists: Stacks stored in list form as strings.
    """
    split_at = list()
    lines = get_input()

    # Split the input at the empty line, which divides the stack diagram from the movelist
    for idx, line in enumerate(lines):
        if line == "":
            split_at.append(line)

    # Take the stack minus the numbers 1-9 at the bottom and reverse it
    # Reversing it puts the bottom row at index 0
    stack = lines[:9][:-1]
    stack.reverse()

    # Take each element in the stack, which is currently a string that looks like '[S] [D]     [W]     [W]     [H] [Q]'
    # Go through each element and divide every 4 characters, using rstrip to get rid of empty space
    # This will make an even list of 9 indices worth of "crates" (either [X] or " ")
    sideways_stack = list()
    for element in stack:
        cargo = [element[idx : idx + 4].rstrip() for idx in range(0, len(element), 4)]
        # Rearrange the crates so that each column is a separate list, so when crates get moved from one column to another
        # we can simply remove and append to the "top" (end) of each
        for idx, crate in enumerate(cargo):
            if crate:
                try:
                    sideways_stack[idx].append(crate)
                except:
                    sideways_stack.append(list())
                    sideways_stack[idx].append(crate)

    return sideways_stack


def sort_moves():
    """Sorts all the moves into lists for iteration. Strips out words and stores only the numbers.
    
    Returns:
        list of lists: Moves stored in lists as [int, int, int]
    """
    lines = get_input()
    moves = list()
    for move in lines[10:]:
        move = move.split(" ")
        command = [int(move[idx : idx + 2][-1]) for idx in range(0, len(move), 2)]
        moves.append(command)

    return moves


def move_crates(move, stacks, as_group=False):
    """Takes the current state of the stacks and moves them according to the move given.
    If multiples is True, then crates will be moved as groups instead of one by one.
    
    Args:
        move (list of int): List of 3 numbers used to move stacks.
        stacks (lists of str): All stacks as strings stored in lists.
        multiples (bool): Move crates as a group or one at a time.
    
    Returns:
        list of lists: Updated stacks stored in list form as strings.
    """
    origin_stack_num = move[1] - 1 # Index 1 is where the crates being moved come from
    destination_stack_num = move[2] - 1 # Index 2 is where the crates being moved go
    number_of_crates = move[0] # Index 0 is the number of crates to move

    # Get the stacks where the crates are moved to and from
    origin_stack = stacks[origin_stack_num]
    destination_stack = stacks[destination_stack_num]

    # Grab the crates that are being moved from the origin stack
    to_move = origin_stack[-number_of_crates:]
    # Choose to move as a group (part 1) or not (part 2))
    if not as_group:
        to_move.reverse()

    # Set the new origin stack by getting rid of the crates being moved
    origin_stack = origin_stack[: len(origin_stack) - number_of_crates]
    # Add the new crates to the destination stack
    destination_stack = destination_stack + to_move

    # Update the full list of stacks
    stacks[origin_stack_num] = origin_stack
    stacks[destination_stack_num] = destination_stack

    return stacks


def rearrange_stacks(as_group=False):
    """The main function to run the whole process of running all moves and sorting the stacks.
    
    Args:
        as_group (bool): True to move crates as a group, Fals to move one by one

    Returns:
        str: String of the last letters in each stack.
    """
    # Get the stacks and all moves to run
    stacks = organize_stacks()
    moves = sort_moves()

    # Iterate through all the moves and feed each move into the move_crates method
    for move in moves:
        stacks = move_crates(move, stacks, as_group)

    return "".join([stack[-1][1] for stack in stacks])


if __name__ == "__main__":
    part_one = rearrange_stacks(as_group=False)
    part_two = rearrange_stacks(as_group=True)
    print("Part 1: {}".format(part_one))
    print("Part 2: {}".format(part_two))
