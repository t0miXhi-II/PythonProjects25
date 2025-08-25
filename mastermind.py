import random

'''
:Possible Update: Add user input validation to ensure that the entered numbers by the players is a 4-digit number
'''

player1 = {
    "name": None,
    "selected_number": None,
    "number_of_guesses": 0,
    "number_of_round_wins": 0
}

player2 = {
    "name": None,
    "selected_number": None,
    "number_of_guesses": 0,
    "number_of_round_wins": 0
}

def main():
    while True:
        game_round()
        print()
        user_response = input("Press ENTER to continue or Q to quit game: ").lower()
        if user_response == "q":
            break
    check_winner(player1["number_of_round_wins"], player2["number_of_round_wins"])
    


def game_round():
    player1["name"] = input("Player 1 - Enter your name: ")
    player2["name"] = input("Player 2 - Enter your name: ")

    #TURN - PLAYER 2
    player1["selected_number"] = input(f"{player1['name']}, Enter any 4 digit number: ")
    print()

    while player2["number_of_guesses"] <= 5:
        guess = ""
        player2_guess = input(f"{player2['name']} Guess the Number: ")
        player2["number_of_guesses"] += 1

        for p1_number in player1["selected_number"]:
            if p1_number in player2_guess:
                guess = guess + p1_number
            else:
                guess = guess + "_"
        
        print(guess)

        if player1["selected_number"] == player2_guess:
            print(f"Correct {player2['name']}!!! You guessed the correct number! - {player2_guess}")
            player2["number_of_round_wins"] += 1
            print()
            break

    #TURN - PLAYER 1
    player2["selected_number"] = input(f"{player2['name']}, Enter any 4 digit number: ")
    print()

    while player1["number_of_guesses"] <= 5:
        guess = ""

        while player1["number_of_guesses"] <= 5:
            guess = ""
            player1_guess = input(f"{player1['name']} Guess the Number: ")
            player1["number_of_guesses"] += 1

            for p2_number in player2["selected_number"]:
                if p2_number in player1_guess:
                    guess = guess + p2_number
                else:
                    guess = guess + "_"


            print(guess)

            if player2["selected_number"] == player1_guess:
                print(f"Correct {player1['name']}!!! You guessed the correct number! - {player1_guess}")
                print()
                break

        if player1["number_of_guesses"] < player2["number_of_guesses"]:
            player1["number_of_round_wins"] += 1
            print(f"{player1['name']} wins this round!")
        elif player2["number_of_guesses"] < player1["number_of_guesses"]:
            player2["number_of_round_wins"] += 1
            print(f"{player2['name']} wins this round!")
        else:
            print("It's a tie!")
        break


def check_winner(player1_attempts: int, player2_attempts: int):
    if player1_attempts > player2_attempts:
        print("Player 1 wins the game!!!")
    elif player2_attempts > player1_attempts:
        print("Player 2 wins the game!!!")
    else:
        print("Draw!!! It's a tie.")


if __name__ == "__main__":
    main()