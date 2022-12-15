from pathlib import Path


def get_input():
    """Parse the input.txt file in the current directory and return the datastream.

    Returns:
        str: The "datastream" which is a long single line of characters
    """
    return Path(__file__).parent.joinpath("input.txt").read_text().split("\n")[0]


def scan_datastream():
    """Scans the datastream and iterates through it as a list to find the first group without duplicate letters.
    
    Returns:
        int, int: Number of characters part one, Number of characters part two
    """
    # Convert the string into a list
    datastream = [*get_input()]
    
    # Iterate through the datastream, using the index of each letter to assess in groups of 4/14
    part_one = None
    part_two = None
    for idx in range(len(datastream)):
        if idx > 2 and not part_one: # Start assesing after the 3rd letter, once there is a full group of 4
            set_of_four = set(datastream[idx-3:idx+1])
            list_of_four = datastream[idx-3:idx+1]
            if len(set_of_four) == len(list_of_four):
                part_one = idx + 1
        if idx > 12 and not part_two: # Start assesing after the 13th letter, once there is a full group of 14
            set_of_fourteen = set(datastream[idx-13:idx+1])
            list_of_fourteen = datastream[idx-13:idx+1]
            if len(set_of_fourteen) == len(list_of_fourteen):
                part_two = idx + 1
        if part_one and part_two:
            break

    return part_one, part_two


if __name__ == "__main__":
    part_one, part_two = scan_datastream()
    print("Part 1: {}".format(part_one))
    print("Part 2: {}".format(part_two))
