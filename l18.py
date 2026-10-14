# Functions
# Lesson 18 - Functions
# Jayden Yiu - l18.py
# 10/14/2026
# *********************
#Import sqrt
from math import sqrt
def four(a:float, b:float)->float:
    #calculate hypotheneuse a^2+b^2=c^2
    #c = sqrt(a^2+b^2)
    return sqrt(a**2-b**2)
#import randint for random range
from random import randint
def five()->None:
    #First var of guessing program
    x=int(input("guess a number(1-100): "))
    #generate number from 1 to 100(inclusive)
    num:int = randint(1,100+1)
    #sets forever until you guess the number
    while x != num:
        #hints for if you guessed too high or low
        if x > num:
            print("You guessed too high")
        else:
            print("You guessed too low")
        #allowing reinput
        x = int(input("Guess a number(1-100): "))
    print("YOU GOT IT!!!!")
    
def six()->None:
    #Second var of guessing program, counts times
    x:int=int(input("guess a number(1-100): "))
    num:int = randint(1,100+1)
    #initialize count variable
    count:int = 1
    while x != num:
        if x > num:
            print("You guessed too high")
        else:
            print("You guessed too low")
        x:int = int(input("Guess a number(1-100): "))
        #increments count
        count+=1
    print("YOU GOT IT!!!!")
    #output how much times it took
    print(f"IT TOOK YOU {count} TIMES")
#imports datetime
from datetime import datetime
def seven()->None:
    #Third var of guessing program, records time taken
    #record start time
    start_time = datetime.now()
    x:int=int(input("guess a number(1-100): "))
    num:int = randint(1,100+1)
    count:int = 1
    while x != num:
        if x > num:
            print("You guessed too high")
        else:
            print("You guessed too low")
        x = int(input("Guess a number(1-100): "))
        count+=1
    print("YOU GOT IT!!!!")
    print(f"IT TOOK YOU {count} TIMES")
    #record end time
    end_time:datetime = datetime.now()
    #record delta between start and end time
    difference = (end_time-start_time)
    #get rid of unnecessary info from difference
    clean_time:str = str(difference).split('.')[0]
    #print how much time it took
    print(f"IT TOOK YOU {clean_time}")

four(3, 4)
five()
six()
seven()
