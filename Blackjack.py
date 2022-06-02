import random as r
import dealer as d
import time as t
import os
import math as m

""" TODO

Insurance
Recognize when dealer or player has blackjack
Saving progress to file

"""


class Hand:
    picture_cards = ['Knight', 'Queen', 'King']
    
    def update_vcards(self):
        self.v_cards = []
        for i in range(len(self.cards)):
            self.v_cards.append(self.cards[i].name)
        return self.v_cards 
    
    def update_value(self):
        self.value = 0
        for i in range(len(self.cards)):
            if self.cards[i].value in Hand.picture_cards:
                self.value = self.value + 10
            elif self.cards[i].value == 'Ace':
                self.value = self.value + 11
            else:
                self.value = self.value + int(self.cards[i].value)
        
        return self.value
    
    def __init__(self, cards) -> None:
        self.cards = cards
        self.v_cards = Hand.update_vcards(self)
        self.value = Hand.update_value(self)
    
    
    def __str__(self):
        return f"Cards in hand: {self.cards}\nVisual cards in hand: {self.v_cards}\nHand value: {self.value}"

def hit(hand, shoe):
    hand.cards.append(shoe.cards.pop())
    hand.update_vcards()
    hand.update_value()


def play_dealer_hand(d_hand, shoe):
    d_hand.v_cards = Hand.update_vcards(d_hand)
    while d_hand.value < 17:
        hit(d_hand, shoe)
    return d_hand


def check_hand(hand, d_hand, shoe, bet, stand):  # Check hand function
    print(hand.value)
    if hand.value > 21:  # Player busts
        d_hand.update_vcards()
        os.system('cls')
        print(f"Dealer hand: {d_hand.v_cards} | Value: {str(d_hand.value)}")
        print(f"\nPlayer hand: {hand.v_cards} | Value: {str(hand.value)}")
        print("\n-------------------")
        print(f'Player Bust! You lost {bet} credits.')
        award = bet * -1
        return award
    
    elif hand.value == 21 or stand == 1 :  # Perfect Hand or Stand
        d_hand = play_dealer_hand(d_hand, shoe)
        os.system('cls')
        print(f"Dealer hand: {d_hand.v_cards} | Value: {str(d_hand.value)}")
        print(f"\nPlayer hand: {hand.v_cards} | Value: {str(hand.value)}")
        print("\n-------------------")
        
        if d_hand.value > hand.value and d_hand.value <= 21:  # Dealer wins
            print(f"Dealer hand beats player hand! You lost {bet} credits.")
            award = bet * -1
            return award
        
        if d_hand.value > 21:  # Dealer loses, bust
            print(f"Dealer bust! You won {bet} credits.")
            award = bet
            return award
        
        if d_hand.value < hand.value:  # Player wins
            # blackjack_cards = ['♣ Ace', '♦ Ace', '♠ Ace', '♥ Ace']
            if hand.value == 21: # and hand.v_cards.contains(''):
                print(f"Blackjack 21! You won {bet} credits.")
                award = bet * 1.5
            else:
                print(f"Player hand beats dealer hand! You won {bet} credits.")
                award = bet
            
            return award
        
        if d_hand.value == hand.value:  # Dealer Push
            print("Dealer Push! You win back your bet.")
            award = 0
            return award
    else:
        award = 0
        return award

def main():  # Main loop
    credits = 1000
    shoe = d.make_shoe_obj(3, 200)
    
    print("Blackjack, by Oliver Marcusson\n")
    t.sleep(1)
    
    while True:
        print(f'You have {credits} credits.')
        print(f'How much do you want to bet? [Max: {m.floor(credits / 2)}]')
        max_bet = m.floor(credits / 2)
        bet = int(input(":"))
        input(f"Bet: {bet} credits | Press ENTER to deal.")
        
        player_hand = Hand([shoe.cards.pop(), shoe.cards.pop()])
        dealer_hand = Hand([shoe.cards.pop(), shoe.cards.pop()])
        dealer_hand.v_cards[0] = 'Hidden'
        
        if dealer_hand.v_cards[1] == '♣ Ace':
            print(f"\nDealer hand: {dealer_hand.v_cards} | Value: ?")
            print("Dealer has an Ace. Do you want to buy insurance? [y / n]")
            insurance = input(':')
            if insurance == 'y':
                credits = credits - m.floor(credits * 0.05)
                 

        while True:
            os.system('cls')
            print(f"Dealer hand: {dealer_hand.v_cards} | Value: ?")
            print(f"\nPlayer hand: {player_hand.v_cards} | Value: {str(player_hand.value)}")
            print("\n-------------------")
            print('\nWhat would you like to do?\n1. Hit\n2. Stand\n3. Double down')
            ans = int(input(":"))
            
            if ans == 1:  # Player hits
                hit(player_hand, shoe)
                award = int(check_hand(player_hand, dealer_hand, shoe, bet, 0))
                credits = credits + award
                if not award == 0:
                    break
                
                
            
            if ans == 2:  # Player stands
                credits = credits + check_hand(player_hand, dealer_hand, shoe, bet, 1)
                break
            
            if ans == 3:  # Player doubles
                bet = bet * 2
                hit(player_hand, shoe)
                credits = credits + check_hand(player_hand, dealer_hand, shoe, bet, 1)
                break
            
        print('\nWould you like to play again? [y / n]')
        ans = input(':')
        if ans == 'n':
            break
        else:
            os.system('cls')
            

if __name__ == "__main__":
    main()