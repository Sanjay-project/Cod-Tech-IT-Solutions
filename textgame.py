def start_game():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself standing at a crossroad.")

    while True:
        print("\nOptions:")
        print("1. Go left")
        print("2. Go right")
        print("3. Stay put")

        choice = input("What do you want to do? Enter the number of your choice: ")

        if choice == 1:
            left_path()
        elif choice == 2:
            right_path()
        elif choice == 3:
            print("You decide to stay put. Nothing eventful happens.")
        else:
            print("Invalid choice. Please enter a valid option.")

def left_path():
    print("\nYou chose to go left. You encounter a mysterious cave.")

    while True:
        print("\nOptions:")
        print("1. Enter the cave")
        print("2. Go back to the crossroad")

        choice = input("What do you want to do? Enter the number of your choice: ")

        if choice == 1:
            enter_cave()
        elif choice == 2:
            start_game()
        else:
            print("Invalid choice. Please enter a valid option.")

def right_path():
    print("\nYou chose to go right. You come across a bridge.")

    while True:
        print("\nOptions:")
        print("1. Cross the bridge")
        print("2. Turn back to the crossroad")

        choice = input("What do you want to do? Enter the number of your choice: ")

        if choice == 1:
            cross_bridge()
        elif choice == 2:
            start_game()
        else:
            print("Invalid choice. Please enter a valid option.")

def enter_cave():
    print("\nYou enter the cave and discover a hidden treasure! Congratulations, you win!")
    play_again()

def cross_bridge():
    print("\nYou cross the bridge and encounter a troll. It demands a toll.")

    while True:
        print("\nOptions:")
        print("1. Pay the toll")
        print("2. Try to fight the troll")

        choice = input("What do you want to do? Enter the number of your choice: ")

        if choice == 1:
            print("You pay the toll and safely cross the bridge.")
            play_again()
        elif choice == 2:
            print("You try to fight the troll, but it's too strong. Game over!")
            play_again()
        else:
            print("Invalid choice. Please enter a valid option.")

def play_again():
    restart = input("\nDo you want to play again? (yes-1/no-0): ")
    if restart == 1:
        start_game()
    elif restart ==0:
        print("Thanks for playing! Goodbye.")
        exit()
    else:
        print("Invalid choice. Exiting the game.")
        exit()

# Start the game
start_game()