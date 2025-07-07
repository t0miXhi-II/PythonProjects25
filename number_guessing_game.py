import random

def main():
    number = get_random_number()
    user_guess = None
    count = 0
    
    while user_guess != number and count < 5:
        try: 
            user_guess = int(input("Guess the number between 1 and 10: "))
        except ValueError as e:
            print("Error:", e)
        else:
            count += 1
            
            if count >= 5:
                print(f"Number of attempts exceeded - {count}")
            else:
                if user_guess < number:
                    print("Too Low")
                elif user_guess > number:
                    print("Too high")
                else:
                    print(f"Congratulation! You have guessed the right number - {number}")


def get_random_number():
    return random.randint(1,10)


if __name__ == "__main__":
    main()