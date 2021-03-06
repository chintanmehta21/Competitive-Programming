'''
Find duplicates in an array when the elements are not less than n-1
'''

def FindDuplicate2(list1):
	res = []
	dup = []
	ifDuplicate = False
	for i in list1:
		if i in res:
			ifDuplicate = True
			dup.append(i)
			continue
		else:
			res.append(i)
			

	if(ifDuplicate == False):
		print("No duplicate elements")
	else:
		print("Duplicates are ", dup)

nums = [13, 90, 95, 91, 13, 97, 88, 84, 88]
FindDuplicate2(nums)