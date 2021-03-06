"""
Leetcode 442 : Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

"""

def FindDuplicate(list1):
	res = []
	for i in range(len(list1)):
		ind = abs(list1[i]) - 1
		if(list1[ind] < 0):
			res.append(ind + 1)
		list1[ind] = -list1[ind]
	return res

nums = [4,3,2,7,8,2,3,1]
nums = FindDuplicate(nums)
print(nums)