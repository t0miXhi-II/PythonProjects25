import turtle

def main():
    artist = turtle.Turtle()
    art_control(artist)

    '''
    for _ in range(4):
        artist.forward(100)
        artist.right(50)
    
    #artist.done()
    input("Press ENTER to end program")
    '''

def art_control(artist: turtle):
    while True:
        user_input = input("Select direction - w(up) | s(down) | a(left) | d(right): ")
        match user_input.lower():
                case "w":
                    artist.forward(50)
                case "s":
                    artist.back(50)
                case "a":
                    artist.left(50)
                case "d":
                    artist.right(50)
                case "q":
                    break
                case _:
                    print("Invalid Input!")
    
    input("Press ENTER to end program")



if __name__ == "__main__":
    main()