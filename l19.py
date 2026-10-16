"""
==============================================================================
l19.py - Guessing Game Exercise
Jayden Yiu
10/16/2026
Python 3.14.7
==============================================================================
Problem Definition – This program is a guessing game program in which the computer chooses at random an integer in the range 1...100.
The user’s goal is to guess the number in the least number of tries. For each incorrect guess the user provides, the computer provides feedback whether the user’s number is too high or too low.
There should always be an option to repeat the game.
Also there should always be error proofing for user input.
Full commenting and headers are required.
Input: Integer from 1-100(inclusive)
Output: The correct number and the attempts plus the time it took
Process: If randint>input, output higher, if randint<input, output lower
==============================================================================
List of Identifiers 
- let start represent the start time from each run of the guessing number game
- let rand represent the random number that the user has to guess
- let inp represent the user input
- let attempts represent that amount of attempts the user took to get the right answer
- let end represent the time the user guessed the correct number
- let delta represent the difference(gap) of start and end
- let repeat_inp represent if the user wants to repeat or not

==============================================================================
"""

# imports randint from the random library to generate 
from random import randint
# imports datetime from datetime for getting current time
from datetime import datetime

#Actual guessing program function, allows reuse by the repeat function
def program()-> None:
    # Saves the start time of this run of the guessing game
    start:datetime = datetime.now()
    # saves the random number from the program so it doesn't change everytime you guess
    rand:int = randint(1, 100)\
    # presets inp(input) as 0, making sure its out of range
    inp:int = 0
    # saves the attempts variable to display later
    attempts:int = 0
    #Endless loop so you have infinite tries to guess
    while inp != rand:
        #try except to clamp the input to 1-100(int)
        try:
            inp:int = int(input("Please try and guess the number between 1-100: "))
            # if input is higher than 100, or lower than 1(out of bounds), raise the error
            if inp > 100 or inp < 1:
                raise ValueError()
        #custom error catching
        except ValueError:
            print("Please provide a valid integer from 1-100")
            #continue used here to prevent clunky code and saves compile time
            continue
        #compares input with random number(feedback for user)
        if inp < rand:
            print("Your guess was too low")
            # adds 1 to the attempts
            attempts+=1
        elif inp > rand:
            print("Your guess was too high")
            # adds 1 to the attempts
            attempts+=1
    # saves end time to calculate delta between start and end time
    end:datetime = datetime.now()
    # delta calculation and formatting
    delta:str = str(end-start).split('.')[0]
    # Tells the user they win
    print(f"You got the number! It was {rand}.")
    # output the amount of attempts it took
    print(f"It took you {attempts} attempts.")
    # output the time they spent to guess the number
    print(f"It took you {delta} to guess the number.")

#function wrapper to repeat the function endless times
def repeat(func) -> None:
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
#calls the repeat program with the guessing program as a parameter
repeat(program)
