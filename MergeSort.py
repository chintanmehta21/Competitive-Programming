"""
Merge Sort uses the Divide and Conquer method to sort the array
The concept of recursion (i.e. function calling itself) is used in Merge Sort
Average-case Time Complexity : O(nlogn)
Worst-case Time Complexity : O(nlogn)
Best-case Time Complexity : O(nlogn)
Worst-case Space Complexity : O(n)
"""

def MergeSort(list1):
	if(len(list1) < 2):
		return list1

	mid = len(list1) // 2
	left = MergeSort(list1[:mid]) 
	right = MergeSort(list1[mid:])
	return Merge(left, right)

def Merge(left, right):
	if(len(left) == 0):
		return right

	if(len(right) == 0):
		return left

	res = []
	left_index = right_index = 0
	while(len(res) < (len(left) + len(right))):
		if(left[left_index] <= right[right_index]):
			res.append(left[left_index])
			left_index += 1
		else:
			res.append(right[right_index])
			right_index += 1

		if(right_index == len(right)):
			res += left[left_index:]
			break

		if(left_index == len(left)):
			res += right[right_index:]
			break

	return res

print("Enter elements with a space : ")
nums = [int(x) for x in input().split()]
print("Original List : ")
print(nums)
nums = MergeSort(nums)
print("Sorted List : ")
print(nums)
