import os
from random import choice
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def play_blackjack():
    os.system('cls')
    print(logo)
    
    player_cards = [choice(cards), choice(cards)]
    computer_cards=[choice(cards), choice(cards)]

    continue_game = True

    while continue_game:
        print(f"       Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"       Computer's first card: {computer_cards[0]}")

        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if sum(player_cards) == 21 and sum(computer_cards) == 21:
                print(f"Your cards: {player_cards}, Final score: {sum(player_cards)}")
                print(f"Computer cards: {computer_cards}, Final score: {sum(computer_cards)}")
                print("   Game Draw.")
                break
        elif sum(player_cards) == 21:
                print(f"Your cards: {player_cards}, Final score: {sum(player_cards)}")
                print(f"Computer cards: {computer_cards}, Final score: {sum(computer_cards)}")
                print("   You Win.")
                break
        elif sum(computer_cards) == 21:
                print(f"Your cards: {player_cards}, Final score: {sum(player_cards)}")
                print(f"Computer cards: {computer_cards}, Final score: {sum(computer_cards)}")
                print("   You Win.")
                break

        if  another_card == "y":
            player_cards.append(choice(cards))
            computer_cards.append(choice(cards))

        else:
            continue_game = False


    game = input("Do you want to play a game of  Blackjack again? Type 'y' or 'n': ")

    if game == 'y':
        play_blackjack()
    else:
        print("Thanks for playing!!!")

    

game = input("Do you want to play a game of  Blackjack? Type 'y' or 'n': ")

if game == 'y':
    play_blackjack()

else:
    print("Bye Bye!!!", sum(cards))


