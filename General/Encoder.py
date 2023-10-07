def create_encoding_sequence() -> dict[str: tuple[str]]:
    return {'suits': ("Spades", "Clubs", "Diamonds", "Hearts"),
            'values': ("bananas", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")}


def encode_cards(cards) -> list:  # (number, suit) 0=spades, 1=clubs, 2=diamonds, 3=hearts
    sequence = create_encoding_sequence()
    suit_conversions = sequence['suits']
    number_conversions = sequence['values']
    return [(number_conversions.index(i.split(" ")[0]), suit_conversions.index(i.split(" ")[-1])) for i in cards]


def decode_cards(cards) -> list:
    sequence = create_encoding_sequence()
    suit_conversions = sequence['suits']
    number_conversions = sequence['values']
    return [number_conversions[i[0]] + " of " + suit_conversions[i[1]] for i in cards]
