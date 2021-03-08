"""
Find how many instances of 5 consecutive zeros in a boolean array
For example: 100000001000001 has 4 instances of 5 consecutive 0's
"""

def findConsecutiveZeros(list1):
	count = 0
	for i in range(len(list1) - 4):
		if list1[i] == 0:
			if (list1[i+1] == 0 and list1[i+2] == 0 and list1[i+3] == 0 and list1[i+4] == 0):
				count += 1

	print("This boolean array has {0} instances of 5 consecutive 0s".format(count))

nums = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
findConsecutiveZeros(nums)
