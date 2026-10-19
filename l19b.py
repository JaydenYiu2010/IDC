# Random Number exercises
# Lesson 19b - Random Number
# Jayden Yiu - l19b.py
# 10/19/2026
# ***************************
from random import randint, shuffle, uniform
def one()->None:
    repeat:bool = True
    diceStats=[0,0,0,0,0,0]
    while repeat:
        diceTotal:int = 0
        dices:list[int] = []
        for i in range(2):
            print(f"Rolling Dice {i+1}")
            dice: int = 0
            for _ in range (4):
                dice = randint(1,6)
                print(dice)
            dices.append(dice)
            diceTotal += dice
            diceStats[dice-1]+=1
            print(f"Final number is {dice}")
        if diceTotal == 2:
            print("You got a Snake Eyes")
        elif diceTotal == 12:
            print("You got Boxcars")
        elif diceTotal == 11:
            print("You got Yo-Eleven")
        elif diceTotal == 7:
            print("You got the Devil")
        print(f"The total score of two dices is {diceTotal}")
        repeat = True if input("Repeat? (Y/N) ").lower() == "y" else False
    counter:int = 1
    for diceStat in diceStats:
        print(f"You rolled {counter} {diceStat} times")
        counter+=1

def two()->None:
    res:list[int]=[]
    streak:int = 0
    streaks:int = 0
    for i in range(100):
        flip:int = randint(0,1)
        res.append(flip)
        if(flip == res[i-1]):
            streak+=1
        else:
            streak = 0
        if streak == 6:
            streaks+=1
    print(f"You had {streaks} streaks that continued over 5")
def three()->None:
    deck = []
    suits = ["Heart", "Diamond", "Club", "Spade"]
    cards = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    for suit in suits:
        for card in cards:
            deck.append(f"{suit} {card}")
    shuffle(deck)
    hand=[]
    for i in range(5):
        print(f"You got a {deck[i]}")
        curr = deck[i].split(" ")[1]
        hand.append(curr)
        if (hand.count(curr) == 2):
            print(f"You got a pair of {curr}")
        elif (hand.count(curr) == 3):
            print(f"You got a three of a kind of {curr}")
def four(n:int)->None:
    circle_points =0
    square_points =0
    pi:float = 0
    for _ in range(n**2):
        rand_x = uniform(-1,1)
        rand_y= uniform(-1,1)
        origin_dist = rand_x**2+rand_y**2
        if origin_dist <= 1:
            circle_points+=1
        square_points +=1
        pi=4*circle_points/square_points
    print(f"pi: {pi}")

one()
two()
three()
four(1000)


