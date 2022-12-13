from pathlib import Path


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    # Split input into a list of lines
    lines = [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]
    return lines


def organize_stacks():
    """
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
        cargo = [element[idx:idx+4].rstrip() for idx in range(0, len(element), 4)]
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
    lines = get_input()
    moves = list()
    for move in lines[10:]:
        move = move.split(" ")
        command = [int(move[idx:idx+2][-1]) for idx in range(0, len(move), 2)]
        moves.append(command)
    
    return moves

def move_crates(move, stacks):
    """ """
    
    origin_stack_num = move[1] - 1
    destination_stack_num = move[2] - 1
    number_of_crates = move[0]

    origin_stack = stacks[origin_stack_num]
    destination_stack = stacks[destination_stack_num]

    to_move = origin_stack[-number_of_crates:]
    to_move.reverse()

    origin_stack = origin_stack[:len(origin_stack)-number_of_crates]

    destination_stack = destination_stack + to_move

    stacks[origin_stack_num] = origin_stack
    stacks[destination_stack_num] = destination_stack
    
    return stacks

def rearrange_stacks():
    stacks = organize_stacks()
    moves = sort_moves()
    
    for move in moves:
        stacks = move_crates(move, stacks)
    
    return stacks
    
if __name__ == "__main__":
    # part_one, part_two = compare_pairs()
    # print("Part 1: {}".format(part_one))
    # print("Part 2: {}".format(part_two))
    stacks = rearrange_stacks()
    last_letter_in_stacks = "".join([stack[-1][1] for stack in stacks])
    print(last_letter_in_stacks)