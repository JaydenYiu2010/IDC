def one() -> int:
    num1 = int(input("Please give number 1: "))
    num2 = int(input("Please give number 2: "))
    for x in range(min(num1, num2),2, -1):
        if(num1 % x == 0 and num2 % x == 0):
            return x
    return 1


def two() -> list[int]:
    nums:list[int] = []
    for _ in range (3):
        nums.append(int(input("Enter a number: ")))
    new_nums:list[int] = []
    for num in nums:
        if len(new_nums) == 0 or num <= new_nums[len(new_nums)-1]:
            new_nums.append(num)
        else:
            for i in range(len(new_nums)):
                if(new_nums[i] < num):
                    new_nums.insert(i, num)
                    break
    return new_nums

print(one())
print(two())
