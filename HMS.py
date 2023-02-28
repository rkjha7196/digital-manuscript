# health management system
import datetime


def current_time():
    return datetime.datetime.now()


print("Press 1 for Harry, 2 for Hammad, 3 for Mohit or 4 for yourself ")
name = int(input())
if name == 1 or name == 2 or name == 3 or name == 4:
    print("Go ahead")
    if name == 4:
        print("Enter your name")
        your_name = input()
    print("Press 1 for Exercise or 2 for Diet")
    # activity = int(input()+"\n")
    while(True):
        activity = int(input())
        if activity != 1 and activity != 2:
            print("enter either 1 or 2")
        else:
            break
    print("Press 1 for Log or 2 to Retrieve")
    # action = int(input())
    while (True):
        action = int(input())
        if action != 1 and action != 2:
            print("enter either 1 or 2")
        else:
            break
    if name == 1 and activity == 1:
        f1 = open("Harry_workouts.txt", "a")
        if action == 1:
            print("What exercise did you do?")
            f1.write(str(current_time())+": "+input()+"\n")
            print("The log has been made successfully")
        elif action == 2:
            f1 = open("Harry_workouts.txt")
            print(f1.read())
    elif name == 1 and activity == 2:
        f2 = open("Harry_diet.txt", "a")
        if action == 1:
            print("What food did you eat?")
            f2.write(str(current_time())+": "+input()+"\n")
            print("The log has been made successfully")
        elif action == 2:
            f2 = open("Harry_diet.txt")
            print(f2.read())
    elif name == 2 and activity == 1:
        f3 = open("Hammad_workouts.txt", "a")
        if action == 1:
            print("What exercise did you do?")
            f3.write(str(current_time())+": "+input()+"\n")
            print("The log has been made successfully")
        elif action == 2:
            f3 = open("Hammad_workouts.txt")
            print(f3.read())
    elif name == 2 and activity == 2:
        f4 = open("Hammad_diet.txt", "a")
        if action == 1:
            print("What food did you eat?")
            f4.write(str(current_time())+": "+input()+"\n")
            print("The log has been made successfully")
        elif action == 2:
            f4 = open("Hammad_diet.txt")
            print(f4.read())
    elif name == 3 and activity == 1:
        f5 = open("Mohit_workouts.txt", "a")
        if action == 1:
            print("What exercise did you do?")
            f5.write(str(current_time())+": "+input()+"\n")
            print("The log has been made successfully")
        elif action == 2:
            f5 = open("Mohit_workouts.txt")
            print(f5.read())
    elif name == 3 and activity == 2:
        f6 = open("Mohit_diet.txt", "a")
        if action == 1:
            print("What food did you eat?")
            f6.write(str(current_time())+": "+input()+"\n")
            print("The log has been made successfully")
        elif action == 2:
            f6 = open("Mohit_diet.txt")
            print(f6.read())
    elif name == 4 and activity == 1:
        f5 = open("your_name_workouts.txt", "a")
        if action == 1:
            print("What exercise did you do?")
            f5.write(str(current_time())+": "+input()+"\n")
            print("The log has been made successfully")
        elif action == 2:
            f5 = open("your_name_workouts.txt")
            print(f5.read())
    elif name == 4 and activity == 2:
        f5 = open("your_name_diet.txt", "a")
        if action == 1:
            print("What exercise did you do?")
            f5.write(str(current_time())+": "+input()+"\n")
            print("The log has been made successfully")
        elif action == 2:
            f5 = open("your_name_diet.txt")
            print(f5.read())

else:
    print("Enter the values between 1, 2, 3 & 4")
