"""
Comparing two adjacent elements and sorting them
Each iteration bubbles the largest element to the end
Average-case time complexity : O(n^2)
Worst-case time complexity : O(n^2)
Best-case time complexity : O(n)
Worst-case Space Complexity : O(1)
"""

def bubble_sort(list1, n):
	for i in range(n):
		array_sorted = True
		for j in range(n - i - 1):
			if(list1[j] > list1[j+1]):
				#swap list1[j] and list1[j+1]
				list1[j], list1[j+1] = list1[j+1], list1[j]
				array_sorted = False
		if array_sorted:
			break
	return list1

nums = []
n = int(input(("Enter n")))
for i in range(n):
	nums.append(int(input()))
print("Original List : ")
print(nums, sep=", ")
print("Sorted List : ")
nums = bubble_sort(nums, n)
print(nums)