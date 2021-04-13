"""
Leetcode #234 : Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst, lst2 = [], []
        while(head):
            lst.append(head.val)
            head = head.next
        for i in reversed(lst):
            lst2.append(i)
        return True if lst == lst2 else False

"""
Efficient Solution : 
	
	def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        reverse = None
        while fast and fast.next:
            reverse, reverse.next, slow, fast = slow, reverse, slow.next, fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if slow.val == reverse.val:
                slow, reverse = slow.next, reverse.next
            else:
                return False
        return True

reverse the first half linked list then compare it with the second half
Time O(L), Space O(1), while L is the length of linked list
"""