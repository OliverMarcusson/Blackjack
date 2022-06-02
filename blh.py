import random as r

card_colors = ['♥', '♠', '♦', '♣']
card_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Knight', 'Queen', 'King', 'Ace']
blackjack = ['Knight', 'Queen', 'King']

def make_deck(decks):
    for i in range(decks):
        deck = []
        for i in range(decks):
            for i in range(4):
                for j in range(13): 
                    deck.append(f"{card_colors[i]} {card_numbers[j]}")
    return deck

ans = None
blackjack_hands = []
for i in range(4):
    for j in range(3):
        string = [f"{card_colors[i]} 'Ace', '{card_colors[i]} {blackjack[j]}'"]
        blackjack_hands.append(string)
        
for i in range(4):
    for j in range(3):
        string = [f"'{card_colors[i]} {blackjack[j]}', {card_colors[i]} 'Ace'"]
        blackjack_hands.append(string)
    
"""
while not ans in blackjack_hands:
    for i in range(10):
        string = [f"{card_colors[r.randint(0,3)]} 'Ace', {card_colors[r.randint(0,3)]} {blackjack[r.randint(0, 2)]}"]
        if not string in blackjack_hands: 
            blackjack_hands.append(string)
            print (string)
    break
"""

print(blackjack_hands)

# [["♥ 'Ace', '♥ Knight'"], ["♥ 'Ace', '♥ Queen'"], ["♥ 'Ace', '♥ King'"], ["♠ 'Ace', '♠ Knight'"], ["♠ 'Ace', '♠ Queen'"], ["♠ 'Ace', '♠ King'"], ["♦ 'Ace', '♦ Knight'"], ["♦ 'Ace', '♦ Queen'"], ["♦ 'Ace', '♦ King'"], ["♣ 'Ace', '♣ Knight'"], ["♣ 'Ace', '♣ Queen'"], ["♣ 'Ace', '♣ King'"], ["'♥ Knight', ♥ 'Ace'"], ["'♥ Queen', ♥ 'Ace'"], ["'♥ King', ♥ 'Ace'"], ["'♠ Knight', ♠ 'Ace'"], ["'♠ Queen', ♠ 'Ace'"], ["'♠ King', ♠ 'Ace'"], ["'♦ Knight', ♦ 'Ace'"], ["'♦ Queen', ♦ 'Ace'"], ["'♦ King', ♦ 'Ace'"], ["'♣ Knight', ♣ 'Ace'"], ["'♣ Queen', ♣ 'Ace'"], ["'♣ King', ♣ 'Ace'"]]