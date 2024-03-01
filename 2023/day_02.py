from pathlib import Path


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(input):
    """Run both parts 1 and 2 in the same loop.
    Parse each game/line and split the string at colon and semicolons to grab id data and "sub game" data (any new set of blue/red/green).
    Process this data to get the sum of all applicable game ids as well as the sum of all "power" values from each game.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:
        int: Sum of IDs (game numbers)
        int: Sum of powers (highest values of red, blue, and green per game multiplied (red * blue * green))
    """
    total_ids = 0  # Part 1 variable for total number of applicable games by id
    total_power = 0  # Part 2 variable for total of all "power" values
    for line in input:
        game_id, sub_games = line.split(":")
        sub_games = sub_games.split(";")

        # Part 1 variables and key, cube_checker used to compare cube numbers to the static value
        game_id = int(game_id.split(" ")[1])
        impossible = False
        cube_checker = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }

        # Part 2 key, most_per_color used to store largest value per cube found in each game
        most_per_color = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }

        for game in sub_games:
            cubes = game.split(",")
            for cube in cubes:
                cube_count, cube_color = cube.strip().split(" ")

                # Part 2: If the number of cubes for the current color is a higher value than already stored, replace the value for that color
                if most_per_color[cube_color] < int(cube_count):
                    most_per_color[cube_color] = int(cube_count)

                # Part 1: If the current game is hasn't been deemed impossible to do, check and make sure the current color is still possible
                if not impossible and cube_checker[cube_color] < int(cube_count):
                    impossible = True

        # Part 1: If a game is found to be possible, add the game id value to the total_ids value
        if not impossible:
            total_ids += game_id

        # Part 2: Multiply the highest values of red, blue, and green cubes to get the "power" then add that to the total_power value
        power_of = (
            most_per_color["red"] * most_per_color["blue"] * most_per_color["green"]
        )
        total_power += power_of

    return total_ids, total_power


if __name__ == "__main__":
    input = get_input()
    part_01, part_02 = do_it(input)
    print("Part 1:", part_01)
    print("Part 2:", part_02)
