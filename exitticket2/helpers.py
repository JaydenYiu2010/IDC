def circumference(radius:float)->float:
    return 3.1415*radius*2
def area(radius:float) ->float:
    return 3.1415*radius**2
def surfaceArea(radius)->float:
    return 4*3.1415*radius**2
def volume(radius:float)->float:
    return (4/3)*3.1415*radius**2
def heightFinder()->float:
    height:float =-1
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
