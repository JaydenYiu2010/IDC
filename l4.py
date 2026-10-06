# For Loops
# Lesson 4 - Counted Loops
# Jayden Yiu - l4.py
# 29/09/2026
# ************************

def one() -> None:
    for _ in range(5):
        x: int = int(input("input a number: "))
        print(x)
def two() -> None:
    sum:int = 0
    for _ in range(5):
        x:int = int(input("Input a number: "))
        sum+=x
        print(x)
    print(sum)
    print(float(sum)/5.0)
def three()-> None:
    x:int = int(input("Please Enter a number: "))
    for i in range(x+1):
        print(i)
def four() -> None:
    print("x|y")
    print("---")
    for i in range(1,10+1):
        x:int = i
        y:int = 2*x+1
        print(f"{x}|{y}")
def five() -> None:
    count:int = 0
    word:str = ""
    while word != "stop":
        word = input("Please enter a word: ")
        count+=1
    print(count)
one()
two()
three()
four()
five()
