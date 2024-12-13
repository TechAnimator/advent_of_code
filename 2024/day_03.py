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

    Returns:
        int, int: Total number of all multiplied pairs added up, Total number of all multiplied pairs added up found after a "do()" instruction 
    '''
    input = get_input()
    
    regex_find_do_chunks = re.compile("(?<=do\(\)).*(?=don't\(\))")
    do_chunks = re.findall(regex_find_do_chunks, input)

    regex_get_mul = re.compile("mul\([0-9]+,[0-9]+\)")
    all_muls = re.findall(regex_get_mul, input)
    
    regex_get_numbers = re.compile("\d+")
    total = 0
    for mul in all_muls:
        numbers = list(map(int, re.findall(regex_get_numbers, mul)))
        multiplied = math.prod(numbers)
        total += multiplied

    total_for_enabled = 0

    return total, total_for_enabled


if __name__ == '__main__':
    total, total_for_enabled = do_it()
    print("Part 1:", total)
    print("Part 2:", total_for_enabled)
