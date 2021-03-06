'''
Find the highest and the lowest element in an array
Input : [11, 23, 12, 45, 14, 19]
Output : Highest = 45 and Lowest = 11
'''

def findHighestLowest(list1):
	highest = list1[0]
	lowest = list1[0]

	for i in list1:
		if i > highest:
			highest = i
		elif i < lowest:
			lowest = i

	print("Highest = {0} and Lowest = {1}".format(highest, lowest))

nums = []
n = int(input("Enter n"))
print("Enter the list")
for i in range(n):
	nums.append(input())
findHighestLowest(nums)