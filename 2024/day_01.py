from pathlib import Path


def get_input():
    '''Parse the input text file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    '''
    return [line for line in Path(__file__).parent.joinpath('day_01_input.txt').read_text().split('\n')]


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
    
    list_a = list()
    list_b = list()

    for line in input:
        number_a, number_b = line.split()
        list_a.append(int(number_a))
        list_b.append(int(number_b))

    list_a.sort()
    list_b.sort()

    # Part 1
    paired_lists = list(zip(list_a, list_b))

    total_distance = 0
    for pair in paired_lists:
        total_distance += abs(pair[0] - pair[1])

    # Part 2
    similarity_score = 0
    for number in list_a:
        similarity_score += (list_b.count(number) * number)

    return total_distance, similarity_score


if __name__ == '__main__':
    total_distance, similarity_score = do_it()
    print("Part 1:", total_distance)
    print("Part 2:", similarity_score)
