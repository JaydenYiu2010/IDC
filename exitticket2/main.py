"""
==================================================
main.py
Jayden Yiu
10-27-2026
Python, 3.14.7
===================================================
Problem Definition – A menu that lets you select different properties of shapes that contains circles.
Input: choice(integer), radius(float), height(float)
Output: The selected property of the shape
Process: pi*radius^2, 4*pi*radius^2, 4/3*pi*radius^2, pi*radius*2
===================================================
List of Identifiers
- let choice be the options of the different properties[1-7]
- let radius represent the radius of the shape
- let heigh represent the height of the cylinder
===================================================
"""

#import helper functions which contains logic for the shapes
from helpers import circumference, area, surfaceArea, volume, surfaceAreaC, volumeC


"""
The menu option uses the helpers functions from my "helpers" module
Args: N/A
Returns:
the return value is none, as it prints all the outputs
"""
def menu()->None:
    # Shows options for properties
    print("Select which options you would like below")
    print("1)  Circumference of a Circle")
    print("2)  Area of a Circle")
    print("3)  Surface Area of a sphere")
    print("4)  Volume of a sphere")
    print("5)  Surface Area of a cylinder")
    print("6)  Volume of a cylinder")
    print("7) Exit")
    # pre-sets variables to 0
    choice=0
    radius=0
    try:
        # Get user input from choice
        choice=int(input("Pick an option [1-7]: "))
        # Prechecks if user wants to exit
        if choice == 7:
            return
        # get user input for radius
        radius=float(input("Provide Radius: "))
        # checks if radius is negative
        if radius <= 0:
            raise ValueError("radius cannot be under 0")
    except ValueError:
        print("Please provide a valid type")
        menu()
        return
    #checks which option you chose
    match choice:
        case 1:
            print(f"circumference of circle: {circumference(radius):.2f}")
        case 2:
            print(f"area of circle: {area(radius):.2f}")
        case 3:
            print(f"surface area of sphere: {surfaceArea(radius):.2f}")
        case 4:
            print(f"volume of sphere: {volume(radius):.2f}")
        case 5:
            print(f"surface area of cylinder: {surfaceAreaC(radius):.2f}")
        case 6:
            print(f"volume of cylinder: {volumeC(radius):.2f}")
        case _:
            menu()


"""
The repeat function allows any function passed in as a parameter to be repeated
Args: func
Returns:
the return valus is none, as it just calls itself over and over
"""
def repeat(func) -> None:
    # runs function
    func()
    # presets inp to ""
    repeat_inp:str =""
    #make loop so user has to input y or n
    while repeat_inp != "y" and repeat_inp != "n": 
        #prompt to try again
        repeat_inp = input("Would you like to try again? (Y/N) ").lower()
        if repeat_inp == "y":
            #calls it self again
            repeat(func)
        elif repeat_inp == "n":
            #returns nothing
            return


"""
The main function is the driver code, it runs other functions
Args: N/A
Returns:
Nothing since it just calls other functions
"""
def main():
    repeat(menu)

if __name__ == '__main__':
    main()
