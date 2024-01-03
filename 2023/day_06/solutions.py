from pathlib import Path
import re
import math


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(times, distances):
    """Take the times and distances and figure out how many races result in a distance traveled greater than the records.

    Args:
        times (list of int): Length of time each race lasts.
        distancess (list of int): The distance that the boat needs to go further than to be considered a "win."

    Returns:
        int: The product of all win counts per race.
    """
    wins_per_race = list() # Create a list to store the win count of each race in
    
    # Iterate through all corresponding times and distances, counting all winning races
    for time, record_distance in zip(times, distances):
        winning_times_count = 0
        for ms in range(0, time):
            distance_traveled = ms * (time - ms)
            if distance_traveled > record_distance:
                winning_times_count += 1
        wins_per_race.append(winning_times_count)

    return math.prod(wins_per_race)


def part_one(input):
    """Store times and distances in lists of ints.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:
        int: The product of all win counts per race, which is the result of the "do_it" method.
    """
    times = list(map(int, re.findall('\d+', input[0])))
    distances = list(map(int, re.findall('\d+', input[1])))

    return do_it(times, distances)


def part_two(input):
    """Store times and distances as a single time and single distance (both stored in a list) of all numbers merged into one.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:
        int: The product of all win counts per race, which is the result of the "do_it" method.
    """
    times = [int("".join(re.findall('\d+', input[0])))]
    distances = [int("".join(re.findall('\d+', input[1])))]

    return do_it(times, distances)


if __name__ == "__main__":
    input = get_input()

    part_one = part_one(input)
    part_two = part_two(input)

    print("\nPart 1:", part_one)
    print("\nPart 2:", part_two)
