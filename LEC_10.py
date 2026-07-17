#Mini Project
#Guess the number
# import random

# target = random.randint(1,10)

# while True:
#     guess = input(("Guess the number between 1 and 10 or Quit(Q):"))
#     if guess == "Q" or guess == "Quit" or guess == "quit" or guess == "q":
#         print("GAME EXIT")
#         break
#     else:
#         if int(guess) < target:
#             print("low! Try again")
#         elif int(guess) > target:
#             print("high! Try again")
#         else:   
#             print("You guessed it right!")
#             print("-------GAME OVER------- ")
#             break




#Random Password Generator
# import random
# import string

# char1 = random.choice("abcdefghijklmnopqrstuvwxyz")
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(type(string.ascii_letters))
# print(string.digits)
# print(string.punctuation)
# print(string.printable)

# print(random.choice("hello"))

# charValues = string.ascii_letters + string.digits + string.punctuation
# password_len = 10
# password = ""

# for i in range(password_len):
#     password+= random.choice(charValues)
# print(password)


#List comprehension [function for in range(n)]
# charValues = string.ascii_letters + string.digits + string.punctuation
# pass_len = 8
# res = "".join([random.choice(charValues) for i in range(pass_len)])
# print(res)