"""
Searching a sorted array by repeatedly dividing the search interval in half
"""

def BinarySearch(list1, x):
	low = mid = 0
	high = len(list1) - 1

	while(low <= high):
		mid = (low + high) // 2

		if(x < list1[mid]):
			high = mid - 1
		elif(x > list1[mid]):
			low = mid + 1
		else:
			return mid
	return -1

print("Enter sorted list with space between them : ")
nums = [int(x) for x in input().split()]
x = int(input("Enter the element to search : "))
index = BinarySearch(nums, x)
if index != -1:
	print("{0} element was found at position {1}".format(x, index + 1))
else:
	print("Element not found")