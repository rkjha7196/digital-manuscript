# SNAKE WATER GUN
# rule of the game:
# snake drinks water >>> snake wins
# gun shoots snake >>> gun wins
# water malfunctions gun >>> water wins
# def game(choice1, choice2):
#     if choice1 == "snake":
#         if choice2 == "water":
#             com = com+1
#             return print("one point added to the computer\nThe score is",com-you)
#         elif choice2 == "snake":
#             print("it is a draw")
#         else:
#             print("one point added to you")
#             you = you + 1
#             return you
#     elif choice1 == "water":
#         if choice2 == "water":
#             print("it is a draw ")
#         elif choice2 == "snake":
#             print("one point added to you")
#             you_new = you + 1
#             return you_new
#         else:
#             print("one point added to the computer")
#             com_new = com + 1
#             return com_new
#     elif choice1 == "gun":
#         if choice2 == "water":
#             print("one point added to you")
#             # you_new = you+1
#             return 1
#         elif choice2 == "snake":
#             print("one point added to the computer")
#             com_new = com + 1
#             return com_new
#         else:
#             print("it is a draw")
# print("You have to choose between snake, water, gun\nWhat is your choice?")
# import random
# i = 0
# com = 0
# you = 0
# while (True):
#     if i<=10:
#         b = ("snake", "water", "gun")
#         a = random.choice(b)
#         c = input()
#         game(a, c)
#         i = i + 1
#         print("Choose again!")
#     else:
#         break
# print("The game is over! and score is", com )
# print("\t\t\t\t\tWelcome to th game of Snake, Water & Gun\t\t\t\t\t\n"
#       "The rules of the game are:\n"
#       "Snake drinks water >>> Snake  wins\n"
#       "Gun shoots snake >>> Gun wins\n"
#       "Water malfunctions gun >>> Water wins")
# print("You have to choose between snake, water, gun")
# import random
# i = 0
# j = 0
# n = 10
# while(n>0):
#     c = input("Press s for snake, w for water & g for gun\n--> ")
#     #lower(c)
#     s = "snake"
#     w = "water"
#     g = "gun"
#     b = ("snake", "water", "gun")
#     a = random.choice(b)
#     if a == "snake":
#         if c == "w":
#             print("1 point to Computer\n")
#             i = i+1
#         elif c == "g":
#             print("1 point to You\n")
#             j = j+1
#         elif c == "s":
#             print("No one got the point\n")
#         else:
#             print("Enter valid input!!\n")
#             continue
#     elif a == "gun":
#         if c == "s":
#             print("1 point to Computer\n")
#             i = i+1
#         elif c == "w":
#             print("1 point to You\n")
#             j = j+1
#         elif c == "g":
#             print("No one got the point\n")
#         else:
#             print("Enter valid input!!\n")
#             continue
#     elif a == "water":
#         if c == "g":
#             print("1 point to Computer\n")
#             i = i+1
#         elif c == "s":
#             print("1 point to You\n")
#             j = j+1
#         elif c == "w":
#             print("No one got the point\n")
#         else:
#             print("Enter valid input!!\n")
#             continue
#     n = n-1
# print("The score is", j,"-",i)
# if j>i:
#     print("You won the game 😊")
# elif j<i:
#     print("You lost the game ☹")
# else:
#     print("It is a tie 😐")
######################## SNAKE WATER GUN GAME ###########################
import random
print("\t\t\t\t\tWelcome to the game --> Snake, Water & Gun\t\t\t\t\t\n"
      "The rules of the game are:\n"
      "Snake drinks water >>> Snake  wins\n"
      "Gun shoots snake >>> Gun wins\n"
      "Water malfunctions gun >>> Water wins")
i = 0
j = 0
n = 10
while n > 0:
    b = ('s', 'w', 'g')
    a = random.choice(b)
    c = input("Press s for snake, w for water & g for gun\n--> ")
    if (a == 's' and c == 'w') or (a=='w' and c == 'g') or (a=='g' and c == 's'):
        print("1 point added to computer")
        j = j+1
        print(f"Score till now is you {i} & computer {j}\n")
    elif (a == 'w' and c == 's') or (a=='g' and c == 'w') or (a=='s' and c == 'g'):
        print("1 point added to you")
        i = i+1
        print(f"Score till now is you {i} & computer {j}\n")
    elif (a == 'w' and c == 'w') or (a == 'g' and c == 'g') or (a == 's' and c == 's'):
        print("It is a draw")
        print(f"Score till now is you {i} & computer {j}\n")
    else:
        print("Enter valid input!!")
        continue
    n = n-1
print("The score is", i,"-",j)
if i > j:
    print("You won the game 😊")
elif i < j:
    print("You lost the game ☹")
else:
    print("It is a tie 😐")
