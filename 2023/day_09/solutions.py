from pathlib import Path


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]


def do_it(input, part_two=False):
    """
    Method for both parts one and two. Generates all sequences of values that come from each line in the input in order to get the 
    "extrapolated" value (the next number in the given sequence). All of these extrapolated numbers are added together for the answer.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.
        part_two (bool): True if solving part two. False if solving part one.

    Returns:
        int: Sum of all extrapolated values coming from the sequences.
    """
    sum_of_extrapolated_values = 0
    for line in input:
        value_history = [list(map(int, line.split()))] # Store the list of values in a list
        current_values = value_history[0].copy() # Copy the first list to start the iteration with
        all_zero = False # Variable that only sets to True when all numbers in a sequence hit 0

        while not all_zero:
            differences = list() # Store values here for the next sequence
            for idx, value in enumerate(current_values):
                if idx == len(current_values)-1:
                    break
                # Next value minus the current gets the new number in the next sequence
                differences.append(current_values[idx+1] - value)
            value_history.append(differences) # Add the completed new sequence of differences to the master list
            all_zero = all(v == 0 for v in differences) # Check if all values are 0 (if True, it ends the while loop)
            
            # If there are non-zero values, set up for another round and go again
            if not all_zero:
                current_values = differences.copy()
        
        
        # Go through the value history from the line of zeros, calculating the extra number in the sequence until you find the
        # value we need in the first sequence/line
        extrapolated_value = 0
        value_history.reverse()
        for values in value_history:
            if part_two:
                extrapolated_value = values[0] - extrapolated_value # Part 2
            else:
                extrapolated_value += values[-1] # Part 1
        
        sum_of_extrapolated_values += extrapolated_value # Add the found value to the main total
    
    return sum_of_extrapolated_values


if __name__ == "__main__":
    input = get_input()

    part_one = do_it(input)
    part_two = do_it(input, part_two=True)

    print("\nPart 1:", part_one)
    print("\nPart 2:", part_two)
