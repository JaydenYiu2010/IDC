# Lesson 1 - 3 exercies
# name, mark avg, and area of circle making
# Jayden Yiu - script.py
# 24/09/2026
# *****************************************

def one() -> None:
    name:str = input("give name pls: ")
    print(name)
def two() -> None:
    name:str = input("give name pls: ")
    marks:list[float] = []
    marks.append(float(input("give mark 1: ")))
    marks.append(float(input("give mark 2:")))
    marks.append(float(input("give mark 3 pls: ")))
    total: float = 0
    for mark in marks:
        total+=mark
    print(name, total/len(marks))
def three() -> None:
    pi:float = 3.14159
    radius:float = float(input("give radius: "))
    print(f"area: {pi*radius**2}")
one()
two()
three()
