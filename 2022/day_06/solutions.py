from pathlib import Path


def get_input():
    """Parse the input.txt file in the current directory and return the datastream.

    Returns:
        str: The "datastream" which is a long single line of characters
    """
    return Path(__file__).parent.joinpath("input.txt").read_text().split("\n")[0]


def scan_datastream():
    """ """
    datastream = [*get_input()]

    for idx, letter in enumerate(datastream):
        if idx > 2:
            set_of_four = set(datastream[idx-3:idx+1])
            list_of_four = datastream[idx-3:idx+1]
            if len(set_of_four) == len(list_of_four):
                part_one = idx + 1
                break
    for idx, letter in enumerate(datastream):
        if idx > 12:
            set_of_fourteen = set(datastream[idx-13:idx+1])
            list_of_fourteen = datastream[idx-13:idx+1]
            if len(set_of_fourteen) == len(list_of_fourteen):
                part_two = idx + 1
                break
    
    return part_one, part_two

if __name__ == "__main__":
    part_one, part_two = scan_datastream()
    print("Part 1: {}".format(part_one))
    print("Part 2: {}".format(part_two))
