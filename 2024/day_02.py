from pathlib import Path


def get_input():
    '''Parse the input text file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    '''
    return [line for line in Path(__file__).parent.joinpath('day_02_input.txt').read_text().split('\n')]


def safe_check(numbers):
    sequence_check = all(i < j for i, j in zip(numbers, numbers[1:]))

    if not sequence_check:
        sequence_check = all(i > j for i, j in zip(numbers, numbers[1:]))
    
    if sequence_check:
        return all(abs(i-j) < 4 for i, j in zip(numbers, numbers[1:]))


def problem_dampener(numbers):
    return


def do_it():
    '''Run both part 1 and 2 in the same call. Store the two numbers from each line into separate lists then sort both lists.
    
    For part 1:
    Pair the two lists and find the difference between each unique pair, adding the value of the difference to the total.
    
    For part 2:
    Iterate through each number in list a, then multiply the number of occurrences in list b by the number itself.

    Returns:
        int, int: Total distance (part 1 answer), similarity score (part 2 answer)
    '''
    input = get_input()
    
    safe_counter = 0
    fixed_counter = 0
    for line in input:
        numbers = list(map(int, line.split()))
        if safe_check(numbers):
            safe_counter += 1
        else:
            problem_dampener(numbers)

    return safe_counter, safe_counter + fixed_counter


if __name__ == '__main__':
    safe_counter, new_safe_counter = do_it()
    print("Part 1:", safe_counter)
    print("Part 2:", new_safe_counter)
