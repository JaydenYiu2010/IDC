# Nested Selection Ex1-3
# Lesson 10 - Nested Selection
# Jayden Yiu - l10.py
# 10/06/2026
# ****************************

# NO AI USED! FEEL FREE TO QUIZ ME ON EACH PART OF THE CODE

# parse_int function to cast str into int with error catching
def parse_int(inp:str)->int:
    # make sure not to pass back variable unless its int
    while True:
        try:
            # NO breaks and continues, just return. 
            # This is the most commonly used standard, strip to make sure that no blank spaces are before or after in the string
            return int(inp.strip())
        # "catching" the error python throws when it fails to cast a type
        except ValueError:
            # error message
            print("Could not cast into int")
            # lets the user reinput, so they can eventually get it right
            inp = input("Please enter a VALID INTEGER: ")

# Ex 1.
def one()->None:
    # user input after calling parse_int function on input()
    x:int = parse_int(input("Please input a integer: "))

    # checks if the value of x is NOT None
    if x != None:
        # standard modulo to see if number is odd or even
        if x % 2 == 0:
            # lets the user know the number is even
            print("This number is even")
        else:
            #lets the user know the number is odd
            print("This number is odd")
# Ex 2.
def two()->None:
    # user input 1 after calling parse_int function on input()
    num1:int = parse_int(input("Please give numerator(integer): "))
    # user input 2 after calling parse_int function on input()
    num2:int = parse_int(input("Please give denominator(integer): "))
    # try to divide by num2 to confirm it isn't a zero, which would cause an error
    try:
        _:int = num1%num2
    except ZeroDivisionError:
        print("Cannot divide by 0, please try again")
        #restarts Ex 2.
        return two()
    # make sure both user inputs are not `None`, technically not needed but used since exercise revolved around nested selection
    if num1!=None and num2 !=None:
        # check if there is any remainder, none then fully divisble
        if num1 % num2 == 0:
            print("The numerator is divisible by the denominator.")
            # `f` is used in newer versions of python that does the same as the `.format()` function, 
            # allowing developers to put values RIGHT IN the string without external functions, mimicking javascript
            print(f"{num1}/{num2} = {num1//num2}")
        else:
            print("The numerator is not fully divisble by the denominator.")
# Ex 3.
def three()->None:
    # user input 1
    num1:int = parse_int(input("Please give numerator(integer): "))
    # user input 2
    num2:int = parse_int(input("Please give denominator(integer): "))
    #try to divide by which number is smaller, confirming it doesn't cause any errors
    try:
        _:int = num1%num2 if num1 > num2 else num2%num1
    except ZeroDivisionError:
        print("Cannot divide by 0, please try again")
        # restart Ex 3.
        return three()
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
        # same as before but switching num2 with num1
        print(num2, "is bigger than", num1)
        
        if num2 % num1 == 0:
           print("The numerator is divisible by the denominator.")
           print(f"{num2}/{num1} = {num2//num1}")
        else:
            print("The numerator is not fully divisble by the denominator.")
    # else means it has to be num1 == num2, therefore always returning fully divisble
    else:
        # again, `f` is used so that the `.format()` is not needed at the end, which makes it harder to read
        print(f"{num1} = {num2} so therefore, it would always be fully divisble")
        print(f"{num1}/{num2} = {num1//num2}")

# driver to call Ex 1-3 to be organized
one()
two()
three()
