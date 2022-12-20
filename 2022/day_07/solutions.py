from pathlib import Path


def get_input():
    """Parse the input.txt file in the current directory and return the datastream.

    Returns:
        str: The "datastream" which is a long single line of characters
    """
    return Path(__file__).parent.joinpath("input.txt").read_text().split("\n")[0]




if __name__ == "__main__":
    # print("Part 1: {}".format(part_one))
    # print("Part 2: {}".format(part_two))
    pass