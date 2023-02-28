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
