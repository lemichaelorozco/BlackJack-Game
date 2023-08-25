]suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
values = {'Ace': [1, 11], 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
game_over = False
player_score = 0
dealer_score = 0
bet_amount = 0
player_money = 1000




def main():


    while game_over = False:

        print("Welcome to Blackjack!")
        deck = initialize_deck()
        deck = shuffle_deck(deck)
        player_hand = []    
        dealer_hand = []

        bet_amount = int(input("How much would you like to bet? "))
        player_money -= bet_amount

        player_hand.append(deal_card(deck))
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))

        print("Your hand:")
        display_hand(player_hand)
        print("Dealer's hand:")
        print(dealer_hand[0])
        print("Hidden card")

        if check_blackjack(player_hand, dealer_hand) == True:
            game_over = True
            break  

        while calculate_hand(player_hand) < 21:
            answer = input("Would you like to hit? (Y/N) ")
            if answer.lower() == 'y':
                hit(deck, player_hand)
                print("Your hand:")
                display_hand(player_hand)
                print("Dealer's hand:")
                print(dealer_hand[0])
                print("Hidden card")
            else:
                break

            if calculate_hand(player_hand) > 21: 
                print("You busted. You lose.")
                game_over = True
                break

        while calculate_hand(dealer_hand) < 17:
            hit(deck, dealer_hand)

        print("Your hand:")
        display_hand(player_hand)
        print("Dealer's hand:")
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

    print("Thanks for playing!")


    





















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
                            
        if calculate_hand(player_hand) == 21:
            print("Blackjack! You win!")
            return True
        elif calculate_hand(dealer_hand) == 21:
            print("Dealer has blackjack. You lose.")
            return True
        else:
            return False



def compare_hands(player_hand, dealer_hand):
                                    
         if calculate_hand(player_hand) > calculate_hand(dealer_hand):
            print("You win!")
            return True
        elif calculate_hand(player_hand) < calculate_hand(dealer_hand):
            print("You lose.")
            return True
        else:
            print("Push.")
            return True         



def play_again():
                                            
            answer = input("Would you like to play again? (Y/N) ")
            if answer.lower() == 'y':
                return True
            else:
                return False

