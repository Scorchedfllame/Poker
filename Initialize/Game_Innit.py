def create_deck():
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    deck = []
    for i in range(1, 14):
        for y in range(4):
            if i == 1:
                deck.append(f"Ace of {suits[y]}")
            elif i <= 10:
                deck.append(f"{i} of {suits[y]}")
            elif i == 11:
                deck.append(f"Jack of {suits[y]}")
            elif i == 12:
                deck.append(f"Queen of {suits[y]}")
            elif i == 13:
                deck.append(f"King of {suits[y]}")
    return deck
