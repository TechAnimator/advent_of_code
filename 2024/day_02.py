from pathlib import Path


def get_input():
    '''Parse the input text file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    '''
    return [line for line in Path(__file__).parent.joinpath('day_02_input.txt').read_text().split('\n')]


def safe_check(numbers):
    '''Take in a list of numbers and check to see if they are ascending in order, then descending if not. If the numbers are in
    sequential order either way, check to make sure all numbers are within 3 of the number before and after in the list.

    Returns:
        bool
    '''
    sequence_check = all(i < j for i, j in zip(numbers, numbers[1:]))

    if not sequence_check:
        sequence_check = all(i > j for i, j in zip(numbers, numbers[1:]))
    
    if sequence_check:
        return all(abs(i-j) < 4 for i, j in zip(numbers, numbers[1:]))


def problem_dampener(numbers):
    '''Take in a list of numbers and loops through each one, removing it and running safe_check each time. Returns True if safe_check
    passes at any time.

    Returns:
        bool
    '''
    for i in range(len(numbers)):
        new_numbers = list(numbers)
        new_numbers.pop(i)
        is_safe = safe_check(new_numbers)
        if is_safe:
            return is_safe


def do_it():
    '''Run both part 1 and 2 in the same call. Store the string of numbers from each line into a list.
    
    For part 1:
    Run safe_check and if it returns True, add 1 to safe_counter.
    
    For part 2:
    If safe_check returned False, run the numbers through problem_dampener and if it returns True, add 1 to unsafe_to_safe_counter.

    Returns:
        int, int: Nunmber of safe reports (part 1 answer), Number of new safe reports (part 2 answer)
    '''
    input = get_input()
    
    safe_counter = 0
    unsafe_to_safe_counter = 0
    for line in input:
        numbers = list(map(int, line.split()))
        if safe_check(numbers):
            safe_counter += 1
        else:
            if problem_dampener(numbers):
                unsafe_to_safe_counter += 1

    return safe_counter, safe_counter + unsafe_to_safe_counter


if __name__ == '__main__':
    safe_counter, new_safe_counter = do_it()
    print("Part 1:", safe_counter)
    print("Part 2:", new_safe_counter)
