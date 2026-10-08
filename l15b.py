def program()->None:
    x = 6.0
    while x < 0 or x > 5:
        try:
            x = float(input("Please enter a number from 0 - 5: "))
        except ValueError:
            print("This isn't a number")
    print(x)
program()
