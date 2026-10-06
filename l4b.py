"""
1) Write a program that asks the user for their name and then asks them to enter 5 marks.
The program should then output their average mark with their name.
The program should offer to repeat with a y/n.
i.e
Mark Average program
Please enter your mark:
Please enter your mark:
Please enter your mark:
Please enter your mark:
Please enter your mark:
Processing…
Johnny your average so far is 89%
Would you like to repeat this program y/n?

2) Write a program that will ask the user to enter the length and width of a rectangle. Create a
program that will draw the rectangle usings the the “*” (star) symbol.
******
******
******
3) Extend program 2 to also ask the user for the any character input and draw the rectangle with
the user input. Also extend the program to draw a hollow rectangle only drawing the outline
AAAAA
A A
AAAAA
"""

def one() ->None:
    print("Mark Average program")
    while True:
        name:str = input("Please Enter your Name: ")
        marks:list[float] = []
        for i in range (1,6):
            marks.append(float(input(f"Please enter mark {i}: ")))
        average:float =sum(marks)/len(marks)
        print("Processing...")
        print("Name | Average Mark")
        print(f"{name} | {average}")
        loop=input("Do you wish to restart? (Y/N) ")
        if loop.lower() == "n":
            break
def two()-> None:
    print("Rectangle building program")
    width:int = int(input("Please enter the width of the rectangle: "))
    height:int = int(input("Please enter the height of the rectangle: "))
    for _ in range(height):
        for _ in range(width):
            print("*", end="")
        print()
def three()->None:
    print("Rectangle building program v2")
    character:str = input("What character would you like the rectangle to be printed with: ")[0]
    hollow:bool = True if input("Would you like it to be Hollow: (Y/N)").lower() == "y" else False
    width:int = int(input("Please enter the width of the rectangle: "))
    height:int = int(input("Please enter the height of the rectangle: "))
    for i in range(height):
        for j in range(width):
            if hollow and ((j == 0 or j==width-1) or (i==0 or i==height-1)):
                print(character, end="")
            elif hollow:
                print(" ", end="")
            else:
                print(character, end="")
        print()
one()
two()
three()
