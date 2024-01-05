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
    }

    all_hands = []

    for line in input:
        cards_hand, bid = line.split(" ")
        cards_hand = list(cards_hand)

        
        values_hand = cards_hand.copy()
        for idx, card in enumerate(values_hand):
            card_value = int(card_values.get(card, card))
            values_hand[idx] = card_value

        card_counter = Counter(values_hand)
        
        wild_card = None
        wild_hand = None
        if part_two:
            if 11 in card_counter:
                checker = card_counter.copy()
                del checker[11]
                
                wild_cards = Counter(checker).most_common(2)

                if len(wild_cards) > 1 and wild_cards[0][1] == wild_cards[1][1]:
                    wild_card = max(wild_cards[0][0], wild_cards[1][0])
                elif wild_cards:
                    wild_card = wild_cards[0][0]

                wild_hand = [wild_card if original_value == 11 else original_value for original_value in values_hand]
                values_hand = [1 if original_value == 11 else original_value for original_value in values_hand]

        if not wild_card:
            card_counter = Counter(values_hand).most_common(5)
        else:
            card_counter = Counter(wild_hand).most_common(5)

        card_counter = [count for _, count in card_counter]

        hand_bid_pair = [card_counter, values_hand, int(bid)]
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
