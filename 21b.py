"""
==================================================
Properties of Sphere
Jayden Yiu
10/23/2026
python, 3.14.7
===================================================
Problem Definition – Required to allow users to select what property they would like for a sphere
Input: option, radius
Output: The perimeter, area, surface area or volume of sphere
Process: 2*pi*radius OR pi*radius^2 OR 4*pi*radius^2 OR 4/3 * pi * radius^3
===================================================
List of Identifiers
- let option represent the property the user wants
- let radius represent the radius of the sphere
===================================================
"""

def perimeter(radius:float)->float:
    """
    The perimeter function returns the perimeter of the circle using the formula 2*pi*radius
    Args: radius
    Returns:
    the return value is the perimeter of the sphere/circle
    """
    return 2*3.1415*radius

def area(radius:float)->float:
    """
    The area function returns the area of the circle using the formula pi*radius^2
    Args: radius
    Returns:
    the return value is the area of the circle
    """
    return 3.1415*radius**2

def surfaceArea(radius:float)->float:
    """
    The surfaceArea function returns the surface area of the sphere using the formula 4*pi*radius^2
    Args: radius
    Returns:
    the return value is the surface area of the sphere
    """
    return 4*3.1415*radius**2

def volume(radius:float)->float:
    """
    The volume function returns the volume of the sphere using the formula 4/3*pi*radius^3
    Args: radius
    Returns:
    the return value is the volume of the sphere
    """
    return (4/3)*3.1415*(radius**3)

def menu(option:int, radius:float)->None:
    """
    The menu function allows the user to select which property they would want
    Args: option, radius
    Returns:
    the return value by the corresponding function that it calls(Perimeter, Area, Surface Area, Volume)
    """
    #Using match case(which is quicker than ifs in certain cases) to select which function to run
    match option:
        #Option 1(perimeter)
        case 1:
            return print(f"Perimeter: {perimeter(radius):.2f}")
        #Option 2(Area)
        case 2:
            return print(f"Area: {area(radius):.2f}")
        #Option 3(Surface Area)
        case 3:
            return print(f"Surface Area: {surfaceArea(radius):.2f}")
        #Option 4(Volume)
        case 4:
            return print(f"Volume: {volume(radius):.2f}")
        #Default Case(Everything that is not above)
        case _:
            return print("Invalid option")

def main()->None:
    
    """
    The main function gets the user inputs and pass it on, it is the driver code
    Args: N/A
    Returns:
    has no return value, since it just calls other functions
    """

    #sets radius to 0 on the function scope so you can pass it later
    radius=0
    #same as radius, sets to 0
    option=0
    #Error catching
    try:
        #Get input and parse as float for radius
        radius = float(input("Please give radius for the sphere: "))
        #Get input and parse as int for options
        option = int(input("Which option would you like: perimeter[1], area[2], surface area[3], volume[4]"))
    except ValueError:
        print("Invalid input, please enter the correct type")
        return
    #Calls menu with the option the user wants, along with the radius the user set
    menu(option, radius)


def repeat(func) -> None:
    """
    The repeat function allows any function passed in as a parameter to be repeated
    Args: func
    Returns:
    the return valus is none, as it just calls itself over and over
    """

    # runs function
    func()
    # presets inp to ""
    repeat_inp:str =""
    #make loop so user has to input y or n
    while repeat_inp != "y" and repeat_inp != "n": 
        #prompt to try again
        repeat_inp = input("Would you like to try again? (Y/N)").lower()
        if repeat_inp == "y":
            #calls it self again
            repeat(func)
        elif repeat_inp == "n":
            #returns nothing
            return

if __name__ == "__main__":
    repeat(main)

