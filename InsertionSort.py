"""
Insertion Sort is comparing each element with all the other elements and inserting it in the correct position
Remember with the card-deck shuffling technique
Average-case Time Complexity : O(n^2)
Worst-case Time Complexity : O(n^2)
Best-case Time Complexity : O(n)
Worst-case Space Complexity : O(1)
"""

def InsertionSort(list1):
	for i in range(1, len(list1)):
		key = list1[i]
		j = i - 1
		while(j > 0 and list1[j] > key):
			list1[j + 1] = list1[j]
			j -= 1
		list1[j + 1] = key

print("Enter elements with a space : ")
nums = [int(x) for x in input().split()]
print("Original List : ")
print(nums, sep=", ")
InsertionSort(nums)
print("Sorted List : ")
print(nums, sep=", ")