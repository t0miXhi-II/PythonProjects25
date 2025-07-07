def main():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    operator = input("Select operation (+, -, *, /): ")

    match operator:
        case "+":
            print(add(x, y))
        case "-":
            print(subtract(x, y))
        case "*":
            print(product(x, y))
        case "/":
            print(divide(x, y))
        case _:
            print("Invalid Input")
        

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def product(x, y):    
    return x * y

def divide(x, y):
    return x / y

if __name__ == "__main__":
    main()