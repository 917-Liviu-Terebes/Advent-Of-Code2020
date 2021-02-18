"""
--- Day 22: Crab Combat ---
Strategy:
- Simulate the combat and be careful with recursive calls
"""


def part1(deck1, deck2):
    """
    Part 2 of the problem
    :param deck1: Deck of the first player (List)
    :param deck2: Deck of the second player (List)
    :return: Score of the winner
    """
    # While the decks have cards, play the game
    while len(deck1) and len(deck2):
        # Delete the first card from the decks and add them to the winning player of the match
        card1, card2 = deck1[0], deck2[0]
        del deck1[0]
        del deck2[0]
        if card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])

    # Calculate the score and return it
    sum_val = 0
    winner = deck1 if len(deck1) else deck2
    for i in range(0, len(winner)):
        sum_val += (winner[i] * (len(winner) - i))

    return sum_val


def part2(deck1, deck2):
    """
    Part 2 of the problem
    :param deck1: Deck of the first player (List)
    :param deck2: Deck of the second player (List)
    :return: Score of the winner and the winner
    """
    # Set to remember each played round
    played_cards = set()

    while len(deck1) and len(deck2):
        current_key = (tuple(deck1), tuple(deck2))
        # Rule #1
        if current_key in played_cards:
            return 150, 1
        else:
            played_cards.add(current_key)

        # Rule #2
        card1, card2 = deck1[0], deck2[0]
        del deck1[0]
        del deck2[0]

        # Rule #3
        if card1 <= len(deck1) and card2 <= len(deck2):
            new_deck1 = deck1[:card1]
            new_deck2 = deck2[:card2]
            winner = part2(new_deck1, new_deck2)[1]

            if winner == 1:
                deck1.extend([card1, card2])
            else:
                deck2.extend([card2, card1])

        # Rule #4
        else:
            if card1 > card2:
                deck1.extend([card1, card2])
            else:
                deck2.extend([card2, card1])

    sum_val = 0
    # By rule #1, number 1 wins
    # Compute the sum and return it
    if len(deck1):
        for i in range(0, len(deck1)):
            sum_val += (deck1[i] * (len(deck1) - i))
        return sum_val, 1
    else:
        for i in range(0, len(deck2)):
            sum_val += (deck2[i] * (len(deck2) - i))
        return sum_val, 2


if __name__ == '__main__':
    f = open('input.txt', 'rt')
    players = f.read().split("\n\n")

    player1 = [int(val) for val in players[0].split("\n")[1:]]
    player2 = [int(val) for val in players[1].split("\n")[1:]]

    print("Part 1: ", part1(player1[:], player2[:]))
    print("Part 2: ", part2(player1[:], player2[:])[0])

    f.close()
