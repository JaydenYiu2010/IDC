# Selection and looping exercises
# Lesson 16 - more exercises
# Jayden Yiu - l16.py
# 10/13/2026
# ********************************

#Finding GCF
def one() -> int:
    #User inputs (2 num)
    num1:int = int(input("Please give number 1: "))
    num2:int = int(input("Please give number 2: "))
    #looping from minimum between num1 and num2 to 2, going downwards to optimise search time
    for x in range(min(num1, num2),2, -1):
        #Check if it is fully divisible
        if(num1 % x == 0 and num2 % x == 0):
            return x
    return 1

# INSERTION SORT
def two() -> list[int]:
    #User input list(unsorted)
    nums:list[int] = []
    #3 inputs
    for _ in range (3):
        nums.append(int(input("Enter a number: ")))
    #creates empty sorted list(to be filled in)
    new_nums:list[int] = []
    #looping through numbers in user input list
    for j in range(len(nums)):
        #Checks if it is the first insertion,can't insert when empty, so append
        if j == 0:
            #appends it to new list
            new_nums.append(nums[j])
            #continues to increment j
            continue
        #actual insert logic
        for i in range(len(new_nums)):
            #compares sorted list with current number to see insertion location
            if new_nums[i] < nums[j]:
                #inserts number after finding index
                new_nums.insert(i, nums[j])
                #breaks to avoid dead code
                break
    #returns sorted list
    return new_nums

print(one())
print(two())
