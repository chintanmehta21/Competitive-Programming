"""
Quick Sort also uses the Divide and Conquer method to sort the array
It partitions the array int two (Elements larger than pivot and Elements smaller than pivot)
Average-case Time Complexity : O(nlogn)
Worst-case Time Complexity : O(n^2)
Best-case Time Complexity : O(nlogn)
Worst-case Space Complexity : O(logn)
"""

def QuickSort(list1):
	if len(list1) < 2:
		return list1

	high, same, low = [], [], []
	pivot = list1[len(list1) // 2]

	for i in list1:
		if i < pivot:
			low.append(i)
		elif i == pivot:
			same.append(i)
		elif i > pivot:
			high.append(i)

	return QuickSort(low) + same + QuickSort(high)

print("Enter elements with a space : ")
nums = [int(x) for x in input().split()]
print("Original List : ")
print(nums)
print("Sorted List : ")
nums = QuickSort(nums)
print(nums)