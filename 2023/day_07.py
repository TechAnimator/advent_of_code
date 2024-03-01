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
    """Method for both parts one and two. Part one solves the puzzle using number values as given, part two accounts for Jacks as Jokers worth 1, not 11.

    Args:
        input (list): Input for the puzzle sorted as lines (str) in a list.

    Returns:
        int: Total winnings based on bid values of each hand multipled by the rank of the hands and added up.
    """
    # Create a dict to store values of letter cards
    card_values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
    }

    all_hands = [] # All hands will get added to this list and sorted by rank

    for line in input:
        cards_hand, bid = line.split(" ")
        cards_hand = list(cards_hand) # Store the cards from this line in a list, each element being a single card
        
        # Create a copy of the hand and convert all letters to their integer value (and convert all numbers from str to int)
        values_hand = cards_hand.copy()
        for idx, card in enumerate(values_hand):
            card_value = int(card_values.get(card, card))
            values_hand[idx] = card_value

        card_counter = Counter(values_hand) # Count how many of each type of card in the hand
        
        wild_card = None
        wild_hand = None
        # If it's part two, we only need to do this if any J cards are found in the hand
        if part_two and 11 in card_counter:
            # Create a "checker" dict from the card counter and get rid of any 11s (J's), use this to find the most common card other than a J
            checker = card_counter.copy()
            del checker[11]
            
            # Find the most 2 common cards, since there are 5 cards per hand we can only have a maximum of 2 cards that show up as most frequent
            wild_cards = Counter(checker).most_common(2)

            # If there are 2 cards that are most common, use the higher valued card as the wild card, otherwise just store the single most common card as wild
            if len(wild_cards) > 1 and wild_cards[0][1] == wild_cards[1][1]:
                wild_card = max(wild_cards[0][0], wild_cards[1][0])
            elif wild_cards:
                wild_card = wild_cards[0][0]

            # Create a wild_hand by replacing all 11s (Js) with the wild_card so that we can figure out the new count for that card
            wild_hand = [wild_card if original_value == 11 else original_value for original_value in values_hand]
            # Create a values_hand by replacing all 11s with a 1 value, since they are worth the least when breaking a tie with all other cards
            values_hand = [1 if original_value == 11 else original_value for original_value in values_hand]

        # Count the cards, use the values hand if no wild card is found (part one OR no Js in hadnd) or the wild hand (part two AND Js in hand)
        if not wild_card:
            card_counter = Counter(values_hand).most_common(5)
        else:
            card_counter = Counter(wild_hand).most_common(5)
        card_counter = [count for _, count in card_counter] # Convert dict to list for sorting purposes
        
        # Store a list of 3 elements [card_counter, values_hand, int(bid)]. The card counter is used to sort all hands, the values hand is used to break the ties
        # of hands of the same type. The bid will be used for the final calculation.
        all_hands.append([card_counter, values_hand, int(bid)])
        
    # Sort the list of hands by index 0 first (the hand types), then index 1 next (the tie breaker/card types within each hand).
    all_hands.sort(key = operator.itemgetter(0, 1))

    # Go through all the hands now that they're sorted and calculate the total winnings
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
