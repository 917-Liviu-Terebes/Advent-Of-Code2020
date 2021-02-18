"""
--- Day 25: Combo Breaker ---
Strategy: Merry Christmas!
- Perform the asked computations carefully and you will get the answer
"""


def transform(subject_number, public_key):
    """
    Perform the described transformation
    :param subject_number: Int
    :param public_key: Int
    :return: The loop size
    """
    loop_size = 0
    value = 1
    while value != public_key:
        loop_size += 1
        value = (subject_number * value) % 20201227
    return loop_size


if __name__ == '__main__':
    # No files this time
    card_public_key = 10943862
    door_public_key = 12721030

    card_loop_size = transform(7, card_public_key)
    door_loop_size = transform(7, door_public_key)

    # Get the encryption key
    door_key = 1
    for _ in range(card_loop_size):
        door_key = (door_key * door_public_key) % 20201227
    card_key = 1
    for _ in range(door_loop_size):
        card_key = (card_key * card_public_key) % 20201227

    print("Part 1: ", door_key, card_key)
