from random import choice

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
yn = ['y', 'n']
uc = ['User', "Computer"]
# Function to detect a blackjack
def blackjack(player_cards:list):
    if 11 in player_cards and 10 in player_cards and len(player_cards) == 2:
        return True
    else:
        return False
# Function to check the winner
def winner(user_cards:list,computer_cards:list):
    if blackjack(user_cards) and blackjack(computer_cards):
        return 'Computer'
    elif blackjack(user_cards):
        return 'User'
    elif blackjack(computer_cards):
        return 'Computer'
    elif sum(user_cards) > 21:
        return 'Computer'
    elif sum(computer_cards) > 21:
        return 'User'

def end_of_game_winner(user_cards:list,computer_cards:list):    
    if blackjack(computer_cards):
        return 'Computer'
    elif sum(user_cards) > 21:
        return 'Computer'
    elif sum(computer_cards) > 21:
        return 'User'
    elif sum(user_cards) > sum(computer_cards):
        return 'User'
    elif sum(computer_cards) > sum(user_cards):
        return 'Computer'
    elif sum(computer_cards) == sum(user_cards):
        return 'Tie'
# Function to solve the Ace card problem
def Ace_card(picked_card:int,player_cards:list):
    if picked_card == 11:
        player_cards.append(11)
        if sum(player_cards) > 21:
            return 1
        else:
            return 11
    else:
        return picked_card
# Function that returns a list containing two cards
def two_cards(cards):
    card_list = []
    for i in range(2):
        picked_card = choice(cards)
        while picked_card in card_list:
            picked_card = choice(cards)
        card_list.append(picked_card)
    return card_list

if __name__ == '__main__':
    
    
    
    # Prompting user
    user_input = input("Enter 'y' to start or 'n' to exit: ")
    while not user_input.lower() in yn:
        user_input = input("Wrong choice. Try again.\nEnter 'y' to start or 'n' to exit: ")

    # Storing cards for user and the computer
    loop = 0
    while user_input == 'y':
        
        # Initializing the game
        user_cards = two_cards(cards)
        computer_cards = two_cards(cards)

        # Printing the users card
        print(f"One of computer's cards is: {computer_cards[0]}")
        print(f"\nYour cards are {user_cards} and the total is {sum(user_cards)}")

        # Asking about a hit or pass
        user_input = input("\nHit or pass: [y/n] ")
        while not user_input.lower() in yn:
            user_input = input("\nHit or pass: [y/n] ")
        
        # In case of a hit
        while user_input != 'n':
            loop = 0
            # Assgining a new card to the user
            new_card = choice(cards)
            while new_card in user_cards and new_card != 10:
                new_card = choice(cards)
                
            # Checking for Ace card and assinging value accordingly
            new_card = Ace_card(new_card,user_cards)        
            user_cards.append(new_card)
            
            # Checking if the sum of user cards exceeds 21 or its a blackjack and determining a winner accordingly
            check_winner = winner(user_cards,computer_cards)
            
            # If there was no winner yet
            if check_winner == None:
                
                # Printing the cards and again asking for a hit or pass
                print(f"One of computer's cards is: {computer_cards[0]}")
                print(f"\nYour cards are {user_cards} and the total is {sum(user_cards)}")    
                user_input = input("\nHit or pass: [y/n] ")
                while not user_input.lower() in yn:
                    user_input = input("\nHit or pass: [y/n] ")
            # If there was a winner        
            else:
                print(f"Computer's cards are {computer_cards} which totals as: {sum(computer_cards)}")
                print(f"Your cards are {user_cards} which totals as: {sum(user_cards)}")
                print(f"The winner is: {check_winner}")
                break
        # Asking the user for another game after the game ended with a blackjack or by exceeding 21    
        try:
            if bool(check_winner) == True and loop == 0:
                user_input = input("Do you want to play another game? [y/n]")
                while user_input not in yn:
                    print("Wrong Input, Try again.")
                    user_input = input("Do you want to play another game? [y/n]")
                continue
        except NameError:
            pass
        # Computer picking cards until total is less than or equal to 17 after user chose to pass
        while sum(computer_cards) <= 17:
            new_card = choice(cards)
            while new_card in computer_cards and new_card != 10 :
                new_card = choice(cards)
            new_card = Ace_card(new_card,computer_cards)    
            computer_cards.append(new_card)
        # Checking for a winner or a tie by comparing values
            
        check_winner = end_of_game_winner(user_cards,computer_cards)
        print(f"\nComputer's cards are {computer_cards} which totals as: {sum(computer_cards)}")
        print(f"\nYour cards are {user_cards} which totals as: {sum(user_cards)}")
        if check_winner == 'Tie':
            print("\nIt's a Tie.")
        else:
            print(f"\nThe winner is {check_winner}.\n")
            
        # Asking the user for another game    
        user_input = input("Do you want to play another game? [y/n]")
        while user_input not in yn:
            print("Wrong Input, Try again.")
            user_input = input("Do you want to play another game? [y/n]")    
        loop += 1          