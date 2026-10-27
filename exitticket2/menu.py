def menu()->None:
    print("Select which options you would like below")
    print("1)  Circumference of a Circle")
    print("2)  Area of a Circle")
    print("3)  Surface Area of a sphere")
    print("4)  Volume of a sphere")
    print("5)  Surface Area of a cylinder")
    print("6)  Volume of a cylinder")
    print("7) Exit")
    choice=0
    radius=0
    try:
        choice=int(input("Pick an option [1-7]: "))
        if choice == 7:
            return
        radius=float(input("Provide Radius: "))
        if radius <= 0:
            raise ValueError("radius cannot be under 0")
    except ValueError:
        print("Please provide a valid type")
        menu()
        return
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
        case 7:
            return
        case _:
            menu()
def circumference(radius:float)->float:
    return 3.1415*radius*2
def area(radius:float):
    return 3.1415*radius**2
def surfaceArea(radius):
    return 4*3.1415*radius**2
def volume(radius:float):
    return (4/3)*3.1415*radius**2
def heightFinder()->float:
    height=-1
    while height == -1:
        try:
            height = float(input("Provide Height: "))
            if height <= 0:
                raise ValueError("Height cannot be under 0")
        except ValueError:
            print("Please give a valid height")
            height = -1
    return height

def surfaceAreaC(radius:float)->float:
    height:float = heightFinder()
    return 2*3.1415*radius**2 + 2*3.1415*radius*height
def volumeC(radius:float)->float:
    height:float = heightFinder()
    return 3.1415*radius**2*height
