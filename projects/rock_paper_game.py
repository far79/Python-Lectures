import random
cont = "y"

while cont == "y" or cont == "yes":
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choices(options)[0]
    print(computer_choice)
    user_choice = input("Which option you want to choose(rock/paper/scissor):").lower()


    if user_choice == "rock" and computer_choice == "paper":
        print("You choosed rock\nComputer choosed paper\nComputer wins!")

    elif user_choice == "rock" and computer_choice == "scissor":
        print("You choosed rock\nComputer choosed scissor\nYou win!")

    elif user_choice == "paper" and computer_choice == "rock":
        print("You choosed paper\nComputer choosed rock\nYou win!")

    elif user_choice == "paper" and computer_choice == "scissor":
        print("You choosed paper\nComputer choosed scissor\nComputer win!")

    elif user_choice == "scissor" and computer_choice == "rock":
        print("You choosed scissor\nComputer choosed rock\nComputer wins!")

    elif user_choice == "scissor" and computer_choice == "paper":
        print("You choosed scissor\nComputer choosed paper\nYou win!")

    elif user_choice == computer_choice:
        print("You choosed", user_choice,"\nComputer choose", computer_choice,"\nIt's a tie")

    else:
        print("Invalid option")

    # else:
    #     print("smtg wrong")
    cont = input("do you want to continue(y/n)?:")

