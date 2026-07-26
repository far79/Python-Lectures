cont = "y"
while cont == "y":
    choice = input("do you want to play the number guessing game(y/n):").lower()
    if choice == "y" :
        import random
        num = random.randint(1,10)
        print(num)
        guess = int(input("Guess a number between 1 & 10:"))

        if num != guess:
            while num != guess:
                if num < guess:
                    print("Guessed number is higher")
                    guess = int(input("Guess a number between 1 & 10:"))
            
                elif num > guess:
                    print("Guessed number is lower")
                    guess = int(input("Guess a number between 1 & 10:"))
                
        if num == guess:
                    print("you guessed correct number")

    elif choice == "n":
        print("Exiting")
        cont = "n"

    else:
         print("Invalid input")