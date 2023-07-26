#This is my second attempt at blackjack.
#In my previous version, I was not able to change the the value 
#of an ace card based on the score of the player's hand. 
#To solve this, I essentially have to start from scratch#

import random

deck = {"ace":11, "2":2, "3":3, "4":4, "5":5, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}
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

start = input("Welcome to Blackjack! Press enter to start.")
print ()
deal_player()
deal_dealer()
deal_player()
deal_dealer()

print ("You are dealt a " + str(player_hand[0]) + " and a " + str(player_hand[1]))
print ("The dealer was dealt a " + str(dealer_hand[0]) + " and another card that is face down")
player_score = get_player_score()
dealer_score = get_dealer_score()
if player_score == 21:
    print ("You have 21. You win!")
    exit()
if dealer_score == 21:
    print ("The dealer's second card was a " + str(dealer_hand[1]))
    print("The dealer has 21. The dealer wins.")
    exit()
else:
    turn = input("Your turn! What would you like to do? (stand or hit) ")
    print ()

#placeholder number
n = 2
m = 2

while turn == "hit":
    deal_player()
    print ("The dealer gave you a " + str(player_hand[n])) 
    n+=1
    player_score = get_player_score()
    print ("Your score is now " + str(player_score))
    if player_score > 21 and "ace" in player_hand and deck["ace"] != 1:
        deck["ace"] = 1
        player_score = get_player_score()
        print ("Luckily you have an Ace! Your score is now " + str(player_score))
        continue
    if player_score > 21:
        print()
        print ("You went over 21! You lose")
        print ("The dealer's second card was a " + str(dealer_hand[1]))
        print ("The dealer had a score of " + str(get_dealer_score()))
        exit()
    if player_score == 21:
        print()
        print ("You have 21! You win!")
        exit()
    else:
        decision = input("What would you like to do? (hit or stand) ")
        print ()


print ("The dealer's second card is a " + str(dealer_hand[1]))
dealer_score = get_dealer_score()
print ("The dealer has a score of "+ str(dealer_score))

deck["ace"] = 11

while dealer_score < 17 and player_score < 21:
    deal_dealer()
    print ("The dealer drew a " + str(dealer_hand[m]))
    m += 1
    dealer_score = get_dealer_score()
    print ("The dealer now has a score of " + str(dealer_score))
    if dealer_score >21 and "ace" in dealer_hand and deck["ace"] != 1:
        deck["ace"] = 1
        dealer_score = get_dealer_score()
        print ("The dealer has an ace, so now the dealer's score is " + str(dealer_score))
        continue
if dealer_score == 21:
    print ()
    print ("The dealer has 21! The dealer wins.")
    exit()
if dealer_score > 21:
    print ()
    print ("The dealer busts! You win!")
    exit()

if dealer_score > player_score:
    print()
    print ("The dealer has a higher score. The dealer wins.")
if player_score > dealer_score:
    print()
    print ("You have a higher score than the dealer! You win!")
if player_score == dealer_score:
    print()
    print ("You have the same score as the dealer. That's a push!")
        





