cont = "y"
while (cont == "y"):
    choice = input("do you want to roll the dice(y/n):")
    if choice == "y":
        import random
        a = random.randint(1,6)
        b = random.randint(1,6)
        print("(",a,",",b,")", sep="")

    elif choice == "n":
        print("Exiting...")
        cont = "n"

    else:
        print("invalid input")



