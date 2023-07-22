#This is my second attempt at blackjack.
#In my previous version, I was not able to change the the value 
#of an ace card based on the score of the player's hand. 
#To solve this, I essentially have to start from scratch#

import random

deck = {"ace":1, "2":2, "3":3, "4":4, "5":5, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}
player_hand = []
dealer_hand = []

def deal_player():
    card = random.choice(list(deck.keys()))
    player_hand.append(card)
    
def deal_dealer():
    card = random.choice(list(deck.keys()))
    dealer_hand.append(card)

def get_player_score():
    score = 0
    for item in player_hand:
        score += deck[item]
    return score
    
def get_dealer_score():
    score = 0
    for item in dealer_hand:
        score += deck[item]
    return score

deal_player()
deal_player()
print (player_hand)
get_player_score()
deal_dealer()
deal_dealer()
print (dealer_hand)
get_dealer_score()

start = input("Welcome to Blackjack! Press enter to start.")
print ()
deal_player()
deal_dealer()
deal_player()
deal_dealer()

print ("You are dealt a " + str(player_hand[0]) + " and a " + str(player_hand[1]))
print ("The dealer was dealt a " + str(dealer_hand[0]) + " and another card that is face down")

if get_player_score() == "21":
    print ("You have 21. You win!")
else:
    turn = input("Your turn! What would you like to do? (stand or hit)")

if turn == "stand":

elif turn =="hit":





