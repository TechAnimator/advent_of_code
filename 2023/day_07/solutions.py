from pathlib import Path
import operator
from collections import Counter


def get_input():
    """Parse the input.txt file in the current directory and return lines as a list.

    Returns:
        list: List populated with each line from the input file as a separate element.
    """
    return [line for line in Path(__file__).parent.joinpath("input.txt").read_text().split("\n")]



def do_it(input, part_two=False):
    """

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:
        int: Total winnings.
    """
    card_values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "X": 1,
    }

    all_hands = []

    for line in input:
        hand, bid = line.split(" ")
        hand = list(hand)
        for idx, card in enumerate(hand):

            card_value = int(card_values.get(card, card))
            hand[idx] = card_value
    
        card_counter = Counter(hand)
        card_counter = Counter(hand).most_common(5)
        card_counter = [count for _, count in card_counter]

        hand_bid_pair = [card_counter, hand, int(bid)]
        all_hands.append(hand_bid_pair)
        
    all_hands.sort(key = operator.itemgetter(0, 1))

    total_winnings = 0
    for idx, hand in enumerate(all_hands):
        _, _, bid = hand
        total_winnings += bid*(idx+1)

    return total_winnings


if __name__ == "__main__":
    input = get_input()

    part_one = do_it(input)
    part_two = do_it(input, part_two=True)

    print("\nPart 1:", part_one)
    print("\nPart 2:", part_two)
