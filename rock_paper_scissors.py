import random

def main():
    options = ["rock", "paper", "scissors"]
    
    while True:
        computer_choice = random.choice(options)

        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        try:
            player_input = int(input("Enter Number to Choose: "))
        except ValueError as e:
            print("Error:", e)
        else:
            '''
            if player_input == 1:
                player_input = "rock"
            elif player_input == 2:
                player_input = "paper"
            elif player_input == 3:
                player_input = "scissors"
            elif player_input == 9:
                break
            else:
                print("Error: Invalid Input")
            '''

            if player_input == 9:
                break
            elif player_input in [1, 2, 3]: 
                player_input = options[player_input - 1]
            else: 
                print("Invalid Input. Try Again.")
                continue
            print()
            print(f"You: {player_input} vs Computer: {computer_choice}")


            if player_input == computer_choice:
                print("It's a Draw!!!")
            elif (player_input == "rock" and computer_choice == "scissors") or (player_input == "paper" and computer_choice == "rock") or (player_input == "scissors" and computer_choice == "paper"):
                print("You win!!!")
            else:
                print("Computer Wins!!!")
            
            print()
   
    
if __name__ == "__main__":
    main()