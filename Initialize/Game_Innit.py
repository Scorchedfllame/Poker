def create_deck():
    deck = []
    for i in range(1, 14):
        for y in range(4):
            deck.append((i, y))
    return deck
