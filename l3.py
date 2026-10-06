# While loops
# Lesson 3- while loops
# Jayden Yiu - l3.py
# 25/09/2026
# *********************
import random

def one() -> None:
    while True:
        x:int = int(input("Enter number, negative to exit: "))
        if x < 0:
            break
        print(x)
def two() -> None:
    while True:
        inp:str = input("Enter stop to stop: ")
        if inp.lower() == "stop":
            break
        print(inp)
def three() -> None:
    inp:int = int(input("enter a number: "))
    for i in range (0, inp+1):
        print(i)
def four() -> None:
    number:int = random.randint(1,10)
    inp = 0
    while inp != number:
        inp:int = int(input("Enter the number to guess between 1-10: "))
    print("Yay, you guessed it")
def five() -> None:
    number:int = random.randint(1,10)
    count: int = 0
    inp = 0
    while inp != number:
        count+=1
        inp = int(input("Enter the number to guess between 1-10: "))
    print("Yay, you guessed it")
    print(f"Took you {count} times")
one()
two()
three()
four()
five()
