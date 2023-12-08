from pathlib import Path
import re


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(input):
    """Gather and store the number of matches in each "card" and use the match count to distribute copies of cards.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:
        int: Point total based on the sum of all the matches of numbers found inside the cards.
        int: Point total based on the number of cards that get generated from the original copy + copies added from matches.
    """
    point_total = 0 # Part 1 answer
    input_length = len(input) # Store the length/number of cards

    # Create a dictionary with the legth of input_length, to be used to gather data for part 2
    # Keys as idx numbers, values as 1 (to count for the copy of the first card at that index)
    copies_dict = dict((idx, 1) for idx in range(input_length))

    for idx, line in enumerate(input):
        winning_numbers, my_numbers = line.split(":")[1].split("|") # Grab winning numbers and my numbers from the line
        winning_numbers = [int(num) for num in re.findall(r'\d+', winning_numbers)] # Convert winning numbers to a list of int
        my_numbers = [int(num) for num in re.findall(r'\d+', my_numbers)] # Convert my numbers to a list of int
        matches = set(winning_numbers).intersection(my_numbers) # Find the numbers that occur in both lists
        number_of_matches = len(matches) # Store the number of matches
        
        # If there are matches, add to the point total (part 1) and the copy count (part 2)
        if number_of_matches:
            point_total_card = 1 # First match gets 1 point
            copies_dict[idx+1] += (1*copies_dict[idx]) # For every copy of the current card, add a copy of the next card

            # Iterate thorough the number count for any matches after the first
            for match_counter in range(2, number_of_matches+1):
                point_total_card *= 2 # Multiply the point total by 2 for all matches after the 1st
                if idx+1 < input_length: # Make sure to not go beyond what exists
                    # Add applicable number of copies based on number of matches to the cards that follow the current
                    copies_dict[idx+match_counter] += (1*copies_dict[idx])

            point_total += point_total_card # Part 1 answer, gather the point total of all the cards

    card_total = sum(copies_dict.values()) # Part 2 answer, add up the number copies of all the cards

    return point_total, card_total


if __name__ == "__main__":
    input = get_input()
    part_one, part_two = do_it(input)
    print("Part 1:", part_one)
    print("Part 2:", part_two)
