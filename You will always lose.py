def menu():
    Welcome_List = ["======================================",
        "WELCOME TO ** YOU WILL ALWAYS LOSE ** ",
        "======================================",
        "WIN BIG OR GO HOME WITH NOTHING.......",
        "=======================================================",
        "GET 3 OF THE SAME NUMBER TO WIN DOUBLE WHAT YOU PLAYED",
        "=======================================================",
        ]
    for options in Welcome_List:
        print(options)
menu()
credits = int((input("YOU CURRENTLY HAVE 100 CREDITS, HOW MUCH WOULD YOU LIKE TO PLAY?")))

begin_credits = 100

while True:
    begin_credits = begin_credits - credits

    if credits <= 100:
        print("YOUR NUMBERS ARE.........")
        print("=========================")

        import random

        random1 = random.randint(0, 9)

        random2 = random.randint(0, 9)

        random3 = random.randint(0, 9)

        random_num = [random1, random2, random3]
        print(random_num)

        if random1 == random2 and random2 == random3:
            credits_Won = credits * 2
            new_credits = credits_Won + begin_credits
            print(f"YOU HAVE WON {credits_Won} CREDITS")
            begin_credits = new_credits
            print(f"YOUR NEW TOTAL IS {begin_credits} CREDITS")

        else:
            print("YOU LOST THAT ONE!!!!! HAHA HAHA")
            print("=========================")

        play_again = input("WOULD YOU LIKE TO PLAY AGAIN??? Y/N ").upper()

        if play_again == "N":
            print(f"YOU HAVE CASHED OUT {begin_credits} CREDITS")
            print("COME LOSE AGAIN SOON!!!!! HAHA HAHAHA")
            exit()

        elif play_again == "Y":
            menu()
            credits = int(input(f"YOU CURRENTLY HAVE {begin_credits} CREDITS, HOW MUCH WOULD YOU LIKE TO PLAY?"))

        else:
            print(" ")
            print("PLEASE ENTER Y FOR YES OR N FOR NO")
            print(" ")
            play_again = input("WOULD YOU LIKE TO PLAY AGAIN??? Y/N ").upper()


    if credits > 100:
        print("YOU SEEM TO BE TO BROKE TO DO THAT, GOOD BYE!")
        print("YOU HAVE CASHED OUT 100 CREDITS")
        print("COME LOSE AGAIN SOON!!! HAHAHAHA")
        exit()

    if credits == " ":
        print("PLEASE ENTER A NUMBER, 100 OR LESS")
        menu()
        credits = int(input("YOU CURRENTLY HAVE 100 CREDITS, HOW MUCH WOULD YOU LIKE TO PLAY?"))
