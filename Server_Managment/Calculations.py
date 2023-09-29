def deal(playercount: int, deck: list):
    hands = []
    for i in range(playercount):
        hands.append(deck[:2])
        deck = deck[2:]
    return deck, hands
def river(deck: list):
    return deck[3:], deck[:3]
