def sort(nums) -> list[int]:
    if(len(nums) == 1):
        return nums
    mid = len(nums)//2
    arr1 = sort(nums[0:mid])
    arr2 = sort(nums[mid:len(nums)])
    i=j=idx=0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            nums[idx] = arr1[i]
            i+=1
        else:
            nums[idx]=arr2[j]
            j+=1
        idx+=1
    return nums
import sys
from random import randint
test = []
for _ in range(int(sys.argv[1])):
    test.append(randint(0,100))
print(sort(test))
