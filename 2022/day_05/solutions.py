from pathlib import Path


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    # Result of this list comp looks like: '59-86,85-87'
    lines = [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]
    return lines


def run():
    """
    """
    split_at = []
    lines = get_input()
    for idx, line in enumerate(lines):
        if line == "":
            split_at.append(line)
    
    stack = lines[:9][:-1]
    stack.reverse()

    for element in stack:
        split_string = [element[i:i+4].rstrip() for i in range(0, len(element), 4)]

        print(split_string)

    # Now that I've got everything in even lists, re-arrange so that things are organized as bottom row being the 0 index of each list
    # This will make it easier to move elements to the "top" of each column (but for ease of organization, to the "top" of each row)
    

if __name__ == "__main__":
    # part_one, part_two = compare_pairs()
    # print("Part 1: {}".format(part_one))
    # print("Part 2: {}".format(part_two))

    run() 
