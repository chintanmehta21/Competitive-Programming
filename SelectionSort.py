"""
Selection sort also finds the minimum element in each iteration
Average-case Time Complexity : O(n^2)
Worst-case Time Complexity : O(n^2)
Best-case Time Complexity : O(n^2)
Worst-case Space Complexity : O(1)
"""

def SelectionSort(list1):
	n = len(list1)
	for i in range(n):
		min_id = i
		for j in range(i+1, n):
			if(list1[j] < list1[min_id]):
				min_id = j
		list1[min_id], list1[i] = list1[i], list1[min_id]
	return list1
	
print("Enter elements with a space : ")
nums = [int(x) for x in input().split()]
print("Original List : ")
print(nums)
nums = SelectionSort(nums)
print("Sorted List : ")
print(nums)	