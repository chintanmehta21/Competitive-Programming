"""
An Array of integers is given, both +ve and -ve. You need to find the two elements such that their sum is closest to zero
Input : [1, 60, -10, 70, -80, 85]
Output : -80 and 85
"""


def sumClosestToZero(list1, size):
	if(size < 2):
		print("Invalid Input")

	else:
		min_i, min_j = 0, 0
		min_sum = list1[0] + list1[1]
		for i in range(len(list1)-1):
			for j in range(i+1, len(list1)):
				sum1 = list1[i] + list1[j]
				if(abs(sum1) < abs(min_sum)):
					min_sum = sum1
					min_i = i
					min_j = j

		print("The elements are {0} and {1}. The sum is {2}".format(list1[min_i], list1[min_j], min_sum))

nums = []
n = int(input("Enter n : "))
print("Enter elements of list")
for i in range(n):
	nums.append(int(input()))
sumClosestToZero(nums, n)