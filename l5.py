# Selection
# Lesson 5 - Selection
# Jayden Yiu - l5.py
# 01/10/2026
# ********************
import random
import sys

def one() ->None:
    num:int = random.randint(1, 10)

    x:int = int(input("Guess a number between 1-10: "))
    if x > num:
        print("The number is lower than",x)
    elif x < num:
        print("The number is higher than", x)
    print("You got it!")


def two()-> None:
    num:int = random.randint(1,10)
    x:int = -1
    while x != num:
        x = int(input("Guess a number between 1-10: "))
        if x > num:
            print("The number is lower than",x)
        elif x < num:
            print("The number is higher than", x)
    print("You got it!")

def three()->None:
    login:str = "login"
    pw:str ="login123"
    inp=""
    while inp != login:
        inp=input("Please enter login username: ")
        if inp != login: 
            print("Wrong login")
    for _ in range (3):
        inp = input("Please enter your password: ")
        if inp == pw:
            print("Success!")
            return
        else:
            print("Incorrect! Please try again...")
    print("Login failed, try again later...")
def four()->None:
    min_num:int = sys.maxsize
    max_num:int = -sys.maxsize-1
    for _ in range (10):
        x:int = int(input("Please enter a number: "))
        min_num = min(x, min_num)
        max_num = max(x, max_num)
    print(min_num, max_num)

def five()->None:
    min_value:float = sys.float_info.max
    for i in range (-10, 20):
        x= i*0.1
        y= 3*(x**2)-(2*x)+1
        if y < min_value:
            min_value = y
    print(min_value)
def six() -> None:
    inps: list[str] = []
    inps.append(input("What would you do, give money away, stop doing the quiz, or jump off? (a, b, c, d)")[0])
    inps.append(input("bro I can't keep doing this, just choose one. (a, b, c, d)")[0]) #TODO
    inps.append(input("bro I can't keep doing this, just choose one. (a, b, c, d)")[0]) #TODO
    inps.append(input("bro I can't keep doing this, just choose one. (a, b, c, d)")[0]) #TODO
    inps.append(input("bro I can't keep doing this, just choose one. (a, b, c, d)")[0]) #TODO
    if len(inps) == 5:
        print("you are a idiot")
def repeat(func) -> None:
    func()
    inp:str = input("Would you like to try again? (Y/N)")[0].lower()
    if inp == "y":
        func()
    else:
        return

def seven()->None:
    repeat(one)
    repeat(two)
    repeat(three)
    repeat(four)
    repeat(five)
    repeat(six)
seven()
