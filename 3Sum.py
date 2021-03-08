"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero
Input : [-1,0,1,2,-1,-4]
Output : [[-1,-1,2],[-1,0,1]]
"""

def ThreeSum(list1):
    res = []
    list1.sort()
    
    for i, p in enumerate(list1):
        if(i > 0 and p == nums[i-1]):
            continue

        l, r = i + 1, len(list1) - 1
        while(l < r):
            sum1 = p + list1[l] + list1[r]
            if(sum1 > 0):
                r -= 1
            elif(sum1 < 0):
                l += 1
            else:
                res.append([p, list1[l], list1[r]])
                l += 1
                while(list1[l] == list1[l+1] and l < r):
                    l += 1

    return res

nums = [2, -1, 0, 1, -4, -1]
nums = ThreeSum(nums)
print(nums)
