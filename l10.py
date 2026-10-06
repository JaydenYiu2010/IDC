# Nested Selection Ex1-3
# Lesson 10 - Nested Selection
# Jayden Yiu - l10.py
# 10/06/2026
# ****************************

# NO AI USED! FEEL FREE TO QUIZ ME ON EACH PART OF THE CODE

# helper function to cast str into int with error catching
def helper(inp:str)->int:
    # make sure not to pass back variable unless its int
    while True:
        try:
            # NO breaks and continues, just return, industry standard, strip to make sure that no spaces are before or after
            return int(inp.strip())
        except ValueError:
            # error message
            print("Could not cast into int")
            # lets the user reinput, so they can eventually get it right
            inp = input("Please enter a VALID INTEGER: ")

# Ex 1.
def one()->None:
    # user input after calling helper function on input()
    x:int = helper(input("Please input a integer: "))

    # checks if the type of x is None
    if x != None:
        # standard modulo to see if number is odd or even
        if x % 2 == 0:
            print("This number is even")
        else:
            print("This number is odd")
# Ex 2.
def two()->None:
    # user input 1 after calling helper function on input()
    num1:int = helper(input("Please give numerator(integer): "))
    # user input 2 after calling helper function on input()
    num2:int = helper(input("Please give denominator(integer): "))
    # make sure both user inputs are integers
    if num1!=None and num2 !=None:
        # check if there is any remainder, none then fully divisble
        if num1 % num2 == 0:
            print("The numerator is divisible by the denominator.")
            print(f"{num1}/{num2} = {num1//num2}")
        else:
            print("The numerator is not fully divisble by the denominator.")
# Ex 3.
def three()->None:
    # user input 1
    num1:int = helper(input("Please give numerator(integer): "))
    # user input 2
    num2:int = helper(input("Please give denominator(integer): "))
    # Check if user input 1 is greater than user input 2
    if num1 > num2:
        print(num1, "is bigger than", num2)
        # same as before
        if num1 % num2 == 0:
           print("The numerator is divisible by the denominator.")
           print(f"{num1}/{num2} = {num1//num2}")
        else:
            print("The numerator is not fully divisble by the denominator.")
    # Check if num2 is bigger than num1 instead of the other way around
    elif num2 > num1:
        # same as before
        print(num1, "is bigger than", num2)
    
        if num1 % num2 == 0:
           print("The numerator is divisible by the denominator.")
           print(f"{num1}/{num2} = {num1//num2}")
        else:
            print("The numerator is not fully divisble by the denominator.")
    # else means it has to be num1 == num2, therefore always returning fully divisble
    else:
        print(f"{num1} = {num2} so therefore, it would always be fully divisble")
        print(f"{num1}/{num2} = {num1//num2}")

# driver to call Ex 1-3
one()
two()
three()
