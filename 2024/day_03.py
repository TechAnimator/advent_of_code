from pathlib import Path
import re
import math


def get_input():
    '''Parse the input text file in the current directory and return the string.

    Returns:
        str
    '''
    return Path(__file__).parent.joinpath('day_03_input.txt').read_text()


def do_it():
    '''Run both part 1 and 2 in the same call.
    
    For part 1:
    Find all instances of mul(#,#) then iterate through all of them to multiply both numbers and add to the total.
    
    For part 2:
    Find all do() and don't() instances, then sort them by index in the input string in a dict, with the value as True (do) or False (don't).
    Iterate through all the stored location indicies and store the valid ranges where all mul are enabled. Use these chunks to grab each valid
    substring from the input string and create a new string with only these valid substrings. Use the same method from part 1 at this point to
    get the new total.

    Returns:
        int, int: Total number of all multiplied pairs added up, Total number of all multiplied pairs added up found after a "do()" instruction 
    '''
    input = get_input()
    
    # Part 2 work

    # Get the index in the str input where all do's occur
    do_chunks = [do.start() for do in re.finditer("do\(\)", input)]
    # Get the index in the str input where all don'ts occur
    dont_chunks = [dont.start() for dont in re.finditer("don't\(\)", input)]

    # Add all indicies for both do's and don'ts to a dict, with the key being the index in the str input and value
    # being True if it's the location of a do and False if it's a location of a don't
    enable_disable_guide = {}
    for do_idx in do_chunks:
        enable_disable_guide[do_idx] = True
    for dont_idx in dont_chunks:
        enable_disable_guide[dont_idx] = False
    enable_disable_guide = dict(sorted(enable_disable_guide.items())) # Sort for iterating

    # Start at the beginning of the str input and find all chunks between do and don't instances.
    enabled = True
    last_do = 0
    enabled_chunks = []
    for idx, is_do in enable_disable_guide.items():
        if enabled and not is_do:
            enabled = False
            enabled_chunks.append((last_do, idx))
        elif not enabled and is_do:
            enabled = True
            last_do = idx

    # Create a new str input with only the enabled/valid str chunks
    new_input = str()
    for chunk in enabled_chunks:
        new_input += input[chunk[0]:chunk[1]]

    # Used for both parts 1 and 2
    regex_get_mul = re.compile("mul\([0-9]+,[0-9]+\)") # Regex for finding 'mul(#,#)'
    regex_get_numbers = re.compile("\d+") # Regex to get all numbers

    all_muls = re.findall(regex_get_mul, input)
    new_muls = re.findall(regex_get_mul, new_input)
    
    # Part 1
    total = 0
    for mul in all_muls:
        numbers = list(map(int, re.findall(regex_get_numbers, mul)))
        multiplied = math.prod(numbers)
        total += multiplied

    # Part 2
    total_for_enabled = 0
    for mul in new_muls:
        numbers = list(map(int, re.findall(regex_get_numbers, mul)))
        multiplied = math.prod(numbers)
        total_for_enabled += multiplied

    return total, total_for_enabled


if __name__ == '__main__':
    total, total_for_enabled = do_it()
    print("Part 1:", total)
    print("Part 2:", total_for_enabled)
