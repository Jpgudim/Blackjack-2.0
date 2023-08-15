#This is my second attempt at blackjack.
#In my previous version, I was not able to change the the value 
#of an ace card based on the score of the player's hand. 
#To solve this, I essentially have to start from scratch#

import random
import time

deck = {"ace":11, "2":2, "3":3, "4":4, "5":5, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}
player_hand = []
dealer_hand = []
#list of valid inputs from the user
valid_list = ["hit", "stand"]

def deal_player():
    card = random.choice(list(deck.keys()))
    player_hand.append(card)
    return player_hand
    
def deal_dealer():
    card = random.choice(list(deck.keys()))
    dealer_hand.append(card)
    return dealer_hand

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

def game():
    deck = {"ace":11, "2":2, "3":3, "4":4, "5":5, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}
    player_hand = []
    dealer_hand = []
    #list of valid inputs from the user
    valid_list = ["hit", "stand"]
    print ()
    player_hand = deal_player()
    dealer_hand = deal_dealer()
    player_hand = deal_player()
    dealer_hand = deal_dealer()
    print (player_hand)
    print ("You are dealt a " + str(player_hand[0]) + " and a " + str(player_hand[1]))
    time.sleep(1)
    player_score = get_player_score()
    print ("Your score is " + str(player_score))
    time.sleep(1)
    print ("The dealer was dealt a " + str(dealer_hand[0]) + " and another card that is face down")
    time.sleep(1)
    dealer_score = get_dealer_score()
    if player_score == 21:
        print()
        print ("You have 21. You win!")
        return
    if dealer_score == 21:
        print ("The dealer's second card was a " + str(dealer_hand[1]))
        print("The dealer has 21. The dealer wins.")
        return
    else:
        turn = input("Your turn! What would you like to do? (stand or hit) ")
        while turn.lower() not in valid_list:
            turn = input("Please enter a valid input (hit or stand): ")
        print ()

    #placeholder numbers and check variable to check if ace has changed value
    n = 2
    m = 2
    check = 0

    if player_score > 21 and "ace" in player_hand:
        player_score = 12
        player_hand = []
        deck["ace"] = 1;
        time.sleep(1)
        print ("you have 2 aces, so your score is " + str(player_score))
        check = 1
        n = 0

    while turn == "hit":
        deal_player()
        time.sleep(1)
        print ("The dealer gave you a " + str(player_hand[n])) 
        n+=1
        if check == 1:
            player_score = get_player_score() + 12
        else:
            player_score = get_player_score()
        time.sleep(1)
        print ("Your score is now " + str(player_score))
        if player_score > 21 and "ace" in player_hand and deck["ace"] != 1 and check != 1:
            deck["ace"] = 1
            player_score = get_player_score()
            time.sleep(1)
            print ("Luckily you have an Ace! Your score is now " + str(player_score))
            time.sleep(2)
            if player_score == 21:
                print()
                time.sleep(1)
                print ("You have 21! You win!")
                return
            else:
                turn = input("What would you like to do? (hit or stand) ")
                while turn.lower() not in valid_list:
                    turn = input("Please enter a valid input (hit or stand): ")
                print ()
                if turn == "hit":
                    continue
                elif turn =="stand":
                    continue
        if player_score > 21:
            print()
            time.sleep(1)
            print ("You went over 21! You lose")
            time.sleep(1)
            print ("The dealer's second card was a " + str(dealer_hand[1]))
            time.sleep(1)
            if dealer_hand == ["ace","ace"]:
                print ("The dealer had a score of 12")
            else:
                print ("The dealer had a score of " + str(get_dealer_score()))
            continue_check = 1
            return
        if player_score == 21:
            print()
            time.sleep(1)
            print ("You have 21! You win!")
            return
        else:
            time.sleep(1)
            turn = input("What would you like to do? (hit or stand) ")
            while turn.lower() not in valid_list:
                turn = input("Please enter a valid input (hit or stand): ")
            print ()


    #resetting ace value and check variable from player turn
    deck["ace"] = 11
    check = 0

    time.sleep(1)
    print ("The dealer's second card is a " + str(dealer_hand[1]))
    time.sleep(1)
    dealer_score = get_dealer_score()
    print ("The dealer has a score of "+ str(dealer_score))

    if dealer_score > 21 and "ace" in dealer_hand:
        dealer_score = 12
        dealer_hand = []
        deck["ace"] = 1;
        time.sleep(1)
        print ("The dealer has an ace, so now the dealer's score is " + str(dealer_score))
        check = 1
        m = 0

    while dealer_score < 17 and player_score < 21:
        deal_dealer()
        time.sleep(1)
        print ("The dealer drew a " + str(dealer_hand[m]))
        m += 1
        if check == 1:
            dealer_score = get_dealer_score() + 12
        else:
            dealer_score = get_dealer_score()
        time.sleep(1)
        print ("The dealer now has a score of " + str(dealer_score))
        if dealer_score >21 and "ace" in dealer_hand and deck["ace"] != 1 and check != 1:
            deck["ace"] = 1
            dealer_score = get_dealer_score()
            time.sleep(1)
            print ("The dealer has an ace, so now the dealer's score is " + str(dealer_score))
            time.sleep(1)
            continue
    if dealer_score == 21:
        print ()
        time.sleep(1)
        print ("The dealer has 21! The dealer wins.")
        print()
        return
    if dealer_score > 21:
        print ()
        time.sleep(1)
        print ("The dealer busts! You win!")
        print()
        return
    if dealer_score > player_score:
        print()
        time.sleep(1)
        print ("The dealer has %s, and you have %s" % (dealer_score, player_score))
        time.sleep(1)
        print ("The dealer has a higher score. The dealer wins.")
        print()
    if player_score > dealer_score:
        print()
        time.sleep(1)
        print ("You have %s, and the dealer has %s" % (player_score, dealer_score))
        time.sleep(1)
        print ("You have a higher score than the dealer! You win!")
        print()
    if player_score == dealer_score:
        print()
        time.sleep(1)
        print ("You have %s, and the dealer has %s" % (player_score, dealer_score))
        time.sleep(1)
        print ("You have the same score as the dealer. That's a push!")
        print()


#starting game
start = input("Welcome to Blackjack! Press enter to start.")
game()
continue_game = input("Would you like to play again? (y/n): ")
while continue_game == "y":
    game()
    time.second(1)
    continue_game = input("Would you like to play again? (y/n): ")
if continue_game == "n":
    print()
    time.second(1)
    print ("Thanks for playing!")
    print()
elif continue_game != "y":
    print()
    time.second(1)
    print ("Invalid input. Terminating program.")
    print()



