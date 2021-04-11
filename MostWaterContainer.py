"""
Leetcode #11 : Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai)
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0)
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water
Notice that you may not slant the container

Example 1:
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]
In this case, the max area of water (blue section) the container can contain is 49

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res

"""
My (Inefficent but correct) Solution : 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        sum1 = maxWater = 0
        n = len(height)
        for index1, l1 in enumerate(height):
            for index2 in range(index1+1, n):
                sum1 = min(l1, height[index2])*((index2-index1))
                maxWater = max(maxWater, sum1)
            sum1 = 0
        return maxWater

Not suitable for very large inputs
"""