from pathlib import Path
import re


def get_input():
    '''Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    '''
    return [line for line in Path(__file__).parent.joinpath('input.txt').read_text().split('\n')]


def convert_words_to_numbers(line):
        '''Parse the inputted string and replace any instance of a written out number to include the number value in the string as well.
        Keeps shared words in tact (twone for example becomes two2twone1one so that it is ensured both the 2 and 1 are represented).

        Args:
            line (str): Line of characters and numbers.

        Return:
            str: Line of characters and numbers after conversion of written numbers to numerical values.
        '''
        digit_converter = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero': '0'
        }
        for word, digit in digit_converter.items():
            # Replace each written word with the word twice and the digit in the middle so that shared words remain in tact (twone for example)
            line = line.replace(word, "".join([word, digit, word]))

        return line


def do_it(input, convert_words=False):
    '''Run both part 1 and 2 in the same loop.
    Parse each line to create two digit numbers from integers in each string that need to be added all together to find the answer.
    For part 2, run the line through the "convert_words_to_numbers" method to grab the nececssary added values for each line.
    
    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.
        convert_words (bool): Set to True will convert written words into number values within the string.

    Returns:
        int: Total value of all numbers found from the input.
    '''
    all_numbers = list()

    for line in input:
        # Part 2, set the convert_words arg to True in order to run the conversion of written out words to numerical values
        if convert_words:
            line = convert_words_to_numbers(line)
        digit_list = re.findall(r'\d', line) # Get all single digits from string
        combined_first_and_last = "".join([digit_list[0], digit_list[-1]]) # Create a 2 digit string from index 0 and -1 (will return the same number twice if only one in list)
        two_digit_number = int(combined_first_and_last) # Covert to int
        all_numbers.append(two_digit_number) # Add number to list for totalling at the end

    return sum(all_numbers) # Return the sum of all numbers


if __name__ == '__main__':
    input = get_input()
    print("Part 1:", do_it(input))
    print("Part 2:", do_it(input, convert_words=True))
