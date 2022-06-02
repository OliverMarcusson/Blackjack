import random as r

card_colors = ['♥', '♠', '♦', '♣']
card_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Knight', 'Queen', 'King', 'Ace']


class Shoe:
    def __init__(self, cards) -> None:
        self.cards = cards


class Card:
    def __init__(self, color, value) -> None:
        self.color = color
        self.value = value
        self.name = str(f"{color} {value}")           


def get_random_card():
    return f"{card_colors[r.randint(0,3)]} {card_numbers[r.randint(0,13)]}"


def get_card(color, number):
    return f"{card_colors[color]} {card_numbers[number]}"


def make_deck(decks):
    for i in range(decks):
        deck = []
        for i in range(decks):
            for i in range(4):
                for j in range(14): 
                    deck.append(Card(card_colors[i], card_numbers[j]))
    return deck


def randomize_list(list, cycles):
    rlist = []
    rlist = list
    for i in range(cycles):
        rnum = r.randint(0, len(rlist) - 1)
        rlist.insert(rnum, rlist[-1])
        rlist.pop()
    return list


def make_shoe_obj(decks, cycles):
    deck = make_deck(decks)
    shoe = randomize_list(deck, cycles)
    shoe = Shoe(shoe)
    return shoe


def main():
    print(get_card(0, 13))
    print(get_card(1, 13))
    print(get_card(2, 13))
    print(get_card(3, 13))


if __name__ == "__main__":
    main()