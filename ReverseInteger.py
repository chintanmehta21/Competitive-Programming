"""
LeetCode #7 : Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        s = (x > 0) - (x < 0)
        x = x * s
        while x : 
            result = (result * 10) + (x % 10)
            x //= 10
            
        return 0 if result > ((2**31) - 1) else (result * s)