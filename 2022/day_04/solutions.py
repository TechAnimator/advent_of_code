from pathlib import Path


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    # Result of this list comp looks like: '59-86,85-87'
    lines = [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]
    return lines


def compare_pairs():
    """Compare the range of numbers in each pair to see if one is fully inside the other and/or both share at least
    one similar number.

    Returns:
        int, int: Number of pairs with one pair fully inside the other, Number of pairs with the same number in both
    """
    # Result of this list comp is a 2 index list of numbers as type string: (['50', '89'], ['42', '89'])
    organized_pairs = [(round.split(",")[0].split("-"), round.split(",")[1].split("-")) for round in get_input()]
    
    # Turns the string type numbers from organized_pairs into int: ([50, 89], [42, 89])
    pairs = [((list(map(int, pair[0])), list(map(int, pair[1])))) for pair in organized_pairs]

    # Go through each set of pairs and compare for both fully contained and overlapping numbers
    fully_contained_sets = []
    overlapping_sets = []
    for pair in pairs:
        pair_one = (list(range(pair[0][0], pair[0][1]+1)))
        pair_two = (list(range(pair[1][0], pair[1][1]+1)))
        
        # If the full range of numbers from one pair is fully inside the other, store in a list
        if all(item in pair_one for item in pair_two) or all(item in pair_two for item in pair_one):
            fully_contained_sets.append(pair)

        # If any number is in both ranges, store in a list
        if any(item in pair_one for item in pair_two):
            overlapping_sets.append(pair)

    return len(fully_contained_sets), len(overlapping_sets)
    

if __name__ == "__main__":
    part_one, part_two = compare_pairs()
    print("Part 1: {}".format(part_one))
    print("Part 2: {}".format(part_two))
