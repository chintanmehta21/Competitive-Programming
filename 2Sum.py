"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

def TwoSum(list2, tar):
    len1 = len(list2)
    for i in range(len1):
        for j in range(i+1, len1):
            if(int(list2[i]) + int(list2[j]) == int(tar)):
                return [i, j]


ipstring = input("Enter list seperated by space")
nums = ipstring.split()
target = input("Enter target")
print(TwoSum(nums, target))
