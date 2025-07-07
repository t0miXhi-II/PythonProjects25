import string
import random

def main():
    try:
        length = int(input("Enter password length: "))
    except ValueError as e:
        print("Error:", e)
    else:
        new_password = generate_password(length)
        print(f"New Password: {new_password}")


def generate_password(length: int):
    character_list = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(character_list) for i in range(length))
    return password


if __name__ == "__main__":
    main()