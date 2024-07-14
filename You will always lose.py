def menu():
    # List containing welcome messages and game instructions
    Welcome_List = ["======================================",
        "WELCOME TO ** YOU WILL ALWAYS LOSE ** ",
        "======================================",
        "WIN BIG OR GO HOME WITH NOTHING.......",
        "=======================================================",
        "GET 3 OF THE SAME NUMBER TO WIN DOUBLE WHAT YOU PLAYED",
        "=======================================================",
        ]
    
   # Print each message in the welcome list
    for options in Welcome_List:
        print(options)
        
menu() # Display the menu

# Get the initial amount of credits the user wants to play with
credits = int((input("YOU CURRENTLY HAVE 100 CREDITS, HOW MUCH WOULD YOU LIKE TO PLAY?")))

begin_credits = 100 # Initialize starting credits

# Main game loop
while True:
    # Subtract the amount of credits played from the total credits
    begin_credits = begin_credits - credits

    # Check if the player has enough credits to play
    if credits <= 100:
        print("YOUR NUMBERS ARE.........")
        print("=========================")

        import random

         # Generate three random numbers between 0 and 9
        random1 = random.randint(0, 9)
        random2 = random.randint(0, 9)
        random3 = random.randint(0, 9)

        # Store the random numbers in a list
        random_num = [random1, random2, random3]
        print(random_num)

        # Check if all three numbers are the same (win condition)
        if random1 == random2 and random2 == random3:
            credits_Won = credits * 2
            new_credits = credits_Won + begin_credits
            print(f"YOU HAVE WON {credits_Won} CREDITS")
            begin_credits = new_credits
            print(f"YOUR NEW TOTAL IS {begin_credits} CREDITS")
        else:
            print("YOU LOST THAT ONE!!!!! HAHA HAHA")
            print("=========================")

        # Ask the player if they want to play again
        play_again = input("WOULD YOU LIKE TO PLAY AGAIN??? Y/N ").upper()

        # If the player chooses to stop playing
        if play_again == "N":
            print(f"YOU HAVE CASHED OUT {begin_credits} CREDITS")
            print("COME LOSE AGAIN SOON!!!!! HAHA HAHAHA")
            exit()

        # If the player chooses to play again
        elif play_again == "Y":
            menu()
            credits = int(input(f"YOU CURRENTLY HAVE {begin_credits} CREDITS, HOW MUCH WOULD YOU LIKE TO PLAY?"))

         # If the player enters an invalid option
        else:
            print(" ")
            print("PLEASE ENTER Y FOR YES OR N FOR NO")
            print(" ")
            play_again = input("WOULD YOU LIKE TO PLAY AGAIN??? Y/N ").upper()

    # If the player tries to bet more credits than they have
    if credits > 100:
        print("YOU SEEM TO BE TO BROKE TO DO THAT, GOOD BYE!")
        print("YOU HAVE CASHED OUT 100 CREDITS")
        print("COME LOSE AGAIN SOON!!! HAHA =D")
        exit()

    # If the player enters an invalid input for credits
    if credits == " ":
        print("PLEASE ENTER A NUMBER, 100 OR LESS")
        menu()
        credits = int(input("YOU CURRENTLY HAVE 100 CREDITS, HOW MUCH WOULD YOU LIKE TO PLAY?"))
