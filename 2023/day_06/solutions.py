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
    """
    """
    # Part 1
    times = list(map(int, re.findall('\d+', input[0])))
    distances = list(map(int, re.findall('\d+', input[1])))

    # Part 2
    times = [int("".join(re.findall('\d+', input[0])))]
    distances = [int("".join(re.findall('\d+', input[1])))]

    wins_per_race = []
    for time, record_distance in zip(times, distances):
        winning_times_count = 0
        for ms in range(0, time):
            distance_traveled = ms * (time - ms)
            if distance_traveled > record_distance:
                winning_times_count += 1
        wins_per_race.append(winning_times_count)

    return math.prod(wins_per_race), None


if __name__ == "__main__":
    input = get_input()

    part_one, part_two = do_it(input)

    print("\nPart 1:", part_one)
    print("\nPart 2:", part_two)
