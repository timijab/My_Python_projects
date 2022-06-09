import random

logo = print(""""__________.____       _____  _________  ____  __.      ____.  _____  _________  ____  __.
\______   |    |     /  _  \ \_   ___ \|    |/ _|     |    | /  _  \ \_   ___ \|    |/ _|
 |    |  _|    |    /  /_\  \/    \  \/|      <       |    |/  /_\  \/    \  \/|      <  
 |    |   |    |___/    |    \     \___|    |  \  /\__|    /    |    \     \___|    |  \ 
 |______  |_______ \____|__  /\______  |____|__ \ \________\____|__  /\______  |____|__ \
        \/        \/       \/        \/        \/                  \/        \/        \/""")



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
common = True
while common:
    def Black_jack_game():
        def card_generation():
            """"This function generates a random card from the list of cards"""
            return random.choice(cards)
        # i dont know why i have this dictionary yet
        black_jack = {
            "computer": card_generation(),
            "player": card_generation()
        }
        player_card = []

        def player():
            """"This function generates two cards for player"""
            # this function generates two player cards
            i = 0
            while i < 2:
                player_card.append(card_generation())
                i += 1
            print(f'Your card lineup {player_card}')
        player()

    # getting the random values for the players
    # getting the random values for the computer

        computer_card = []
        def computer():
            """This function generates two cards for dealer or computer"""
            i = 0
            while i < 2:
                computer_card.append(card_generation())
                i += 1
            print(f'Dealers deck {[computer_card[0]]}')
        computer()

        def total_p():
            # combining all the players
            total_player = 0
            for item in player_card:
                total_player += item
            return total_player
        total_p()

        def total_c():
            # combining all the cards for computer or dealer
            total_computer = 0
            for item in computer_card:
                total_computer += item
            return total_computer
        total_c()


        # when the player wants to turn another card
        # Bug alert in case of a draw!!!
        turn_next_card = input('Do you wish to turn another card \nEnter y or n ')
        if turn_next_card.lower() == 'y':
            player_card.append(card_generation())
            total_p()
        elif turn_next_card.lower() == 'n':
            total_p()
        print(f"your card is lined up as {player_card}")


        # As long as card combination for the dealer doesnt amount to > 17
        while total_c() < 17 and total_p() < 21:
            computer_card.append(card_generation())
            total_c()
        print(f"The dealers card is lined up {computer_card}")
        print(f'The total on the dealer is {total_c()}')

        def conditions():
            if total_p() == total_c():
                print('Draw!!!')
            #     Bug alert: this has to return to the loop to try again
                end_of_game = input('Do you wish to try again\nEnter (y) for Yes or (n) for No ')
                if end_of_game.lower() == "y":
                    Black_jack_game()
                elif end_of_game.lower() == 'n':
                    common = False
            elif total_c() == 21:
                print('computer got a black Jack')
                print('computer wins')

            elif total_p() == 21:
                print('you got a black Jack')
                print('You win')


            elif total_p() > 21  and total_c() < 21:
                print(f'Dealer wins, your card accumulates to {total_p()} ')
            elif total_c() > 21 and total_p() < 21:
                print(f'you win with a total of {total_p()}, the dealers accumulates to {total_c()} ')
        conditions()
        # compare who is closet to the marker
        if total_c() > total_p():
            if total_c() < 21:
                print(f'dealer wins with {total_c()} and your card accumlates to {total_p()}')
        if total_p() > total_c():
            if total_p() < 21:
                print(f'you win, your cards accumlates to {total_p()}')

    Black_jack_game()
    end_of_game = input('Do you wish to continue (y) for yes and (n) for no ')
    if end_of_game.lower() == 'n':
        common = False
    elif end_of_game.lower() == "y":
        common = True

