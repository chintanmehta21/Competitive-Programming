"""
Reverse a list using Recursion
"""

def reverse(list1):
    if(len(list1)==0):
        return ([])
    else:
        return [list1[-1]] + reverse(list1[:-1])

print("Enter n")
n = int(input())
list1 = []
print("Enter elements of list")
for i in range(n):
    b = int(input())
    list1.append(b)
print(reverse(list1))
