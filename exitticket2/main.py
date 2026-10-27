from menu import menu


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
        repeat_inp = input("Would you like to try again? (Y/N) ").lower()
        if repeat_inp == "y":
            #calls it self again
            repeat(func)
        elif repeat_inp == "n":
            #returns nothing
            return


def main():
    repeat(menu)

if __name__ == '__main__':
    main()
