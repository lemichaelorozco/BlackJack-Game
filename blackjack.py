suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
values = {'Ace': [1, 11], 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
game_over = False




def main():

    player_score = 0
    dealer_score = 0
    bet_amount = 0
    player_money = 1000
    round_number = 0

    while game_over == False and player_money > 0:

        print("Welcome to Blackjack!")
        print(f"Round {round_number}!")
        round_number += 1
        deck = initialize_deck()
        deck = shuffle_deck(deck)
        player_hand = []    
        dealer_hand = []
        player_win = False
        tie = False
        player_second_hand_win = False
        dealer_win = False



        while True:
            try:
                bet = int(input("Please enter your bet: "))
                break
            except ValueError:
                print("That was not a valid bet. Please enter a number.")


        deal_initial_hands(deck, player_hand, dealer_hand)


        print("Your hand: \n" )
        display_hand(player_hand)
        print("\n")
        print("Dealer's hand: \n")
        print(dealer_hand[0])
        print("Hidden card \n")




        '''Splitting aces logic would occur somewhere around here. After the player's first hand is dealt, they would be asked if they want to split. If they do, the first hand would be dealt a second card, and the second hand would be dealt a second card. Then, the player would play the first hand, and then the second hand. The player would be able to hit or stand on each hand. The dealer would then play their hand. The player would then be paid out for each hand.'''
        if player_hand[0].split()[0] == player_hand[1].split()[0]:
            answer = input("Would you like to split? (Y/N) ")
            if answer.lower() == 'y':
                bet_amount2 = bet_amount
                player_hand2 = []
                player_hand = player_hand[0]
                player_hand.append(deal_card(deck))   
                player_hand2.append(player_hand[1])
                player_hand2.append(deal_card(deck))
                print("Your first hand: \n")
                display_hand(player_hand)
                print("\n")
                print("Your second hand: \n")
                display_hand(player_hand2)
                print("\n")
                print("Dealer's hand: \n")
                print(dealer_hand[0])
                
                '''while calculate_hand(player_hand1) < 21: You can later add the logic for the player to hit or stand on each hand here. For now,
                    we'll just allow the player to hit once on each hand. '''


                while calculate_hand(dealer_hand) <= 17:
                    hit(deck, dealer_hand)



        if calculate_hand(player_hand) == 9 or calculate_hand(player_hand) == 10 or calculate_hand(player_hand) == 11:
            answer = input("Would you like to double down? (Y/N) ")
            if answer.lower() == 'y':
                bet_amount *= 2
                hit(deck, player_hand)

        if calculate_hand(player_hand2) == 9 or calculate_hand(player_hand2) == 10 or calculate_hand(player_hand2) == 11:
            answer = input("Would you like to double down? (Y/N) ")
            if answer.lower() == 'y':
                bet_amount2 *= 2
                hit(deck, player_hand2)


        while calculate_hand(player_hand) < 21:
            answer = input("Would you like to hit? (Y/N) ")
            if answer.lower() == 'y':
                hit(deck, player_hand)
            else:
                break

            if calculate_hand(player_hand) > 21: 
                print("You busted. You lose.")
                game_over = True
                break



        while calculate_hand(dealer_hand) <= 17:
            hit(deck, dealer_hand)



        print("Your hand: \n")
        display_hand(player_hand)
        print("Dealer's hand: \n")
        display_hand(dealer_hand)


        
        if check_blackjack(player_hand, dealer_hand) == True:
            game_over = True
            break

        if compare_hands(player_hand, dealer_hand) == True:
            game_over = True
            break

        if play_again() == False:
            game_over = True
            break   

        if player_money <= 0:
            print("You're out of money! Thanks for playing!")
            game_over = True
            break

    if player_win == True:
        player_money += bet_amount
        player_score += 1
    else:
        player_money -= bet_amount
        dealer_score += 1
        
    if player_second_hand_win == True:
        player_money += bet_amount
        player_score += 1
    else:
        player_money -= bet_amount
        dealer_score += 1   

    print(f"Your money: {player_money}")
    print(f"Round number: {round_number}")
    print(f"Your score: {player_score}")
    print(f"Dealer's score: {dealer_score}")
    print("Thanks for playing!")
    play_again











def initialize_deck():  
    
    deck = []
    for suit in suits:
        for rank in ranks:
            card = f"{rank} of {suit}"
            deck.append(card)

    return deck





def shuffle_deck(deck):
    
        import random
        random.shuffle(deck)
        return deck




def deal_card(deck):
        
        card = deck.pop(0)
        return card
     




def calculate_hand(hand):
        
        hand_value = 0
        for card in hand:
            if card.split()[0] == 'Ace':
                if hand_value + 11 > 21:
                    hand_value += 1
                else:
                    hand_value += 11
            else:
                hand_value += values[card.split()[0]]
        return hand_value



def display_hand(hand):
            
            for card in hand:
                print(card)
            return None




def hit(deck, hand):
                    
    hand.append(deal_card(deck))
    return hand 



def check_blackjack(player_hand, dealer_hand):
                            
        if calculate_hand(player_hand) == 21 and calculate_hand(dealer_hand) == 21:
            print("Tie. Push.")
            tie = True
            return True
        elif calculate_hand(player_hand) == 21:
            print("You have blackjack. You win!")
            player_win = True
            return True
        elif calculate_hand(dealer_hand) == 21:
            print("Dealer has blackjack. You lose.")
            return True
        else:
            return False


def compare_hands(player_hand, dealer_hand):
    player_score = calculate_hand(player_hand)
    dealer_score = calculate_hand(dealer_hand)

    if player_score > 21:
        print("You busted. You lose!")
        return True
    elif dealer_score > 21:
        print("Dealer busted. You win!")
        player_win = True
        return True
    elif player_score == dealer_score:
        print("Tie. Push.")
        tie = True
        return True
    elif player_score > dealer_score:
        print("You win!")
        player_win = True
        return True
    else:
        print("You lose.")
        return True   




def play_again():
                                            
            answer = input("Would you like to play again? (Y/N) ")
            if answer.lower() == 'y':
                return True
            else:
                return False




def deal_initial_hands(deck, player_hand, dealer_hand):
    player_hand.append(deal_card(deck))
    player_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))
    return None





if __name__ == "__main__":
    main()






'''



** Not top priority



** Comments and Documentation: While your code is quite readable, adding comments and documentation can improve maintainability, especially if you or someone else wants to modify the game in the future.

** Function Descriptions: Adding docstrings to your functions describing what they do, their parameters, and return values would be beneficial.


** Graphics or UI Enhancements: While not essential for a console-based game, adding some form of visual enhancement or user interface can make the game more engaging.




-- TO DO:

-- Stage and commit changes to GitHub
-- Push changes to GitHub
-- Add comments and documentation to code
-- Add docstrings to functions
-- Add graphics or UI enhancements
-- Add insurance logic
-- Add surrender logic




'''