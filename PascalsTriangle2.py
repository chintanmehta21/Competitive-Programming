"""
Leetcode #119 : Pascal's Triangle II
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    	triangle = [[1]*(i+1) for i in range(rowIndex + 1)]
    	for i in range(rowIndex + 1):
    		for j in range(1, i):
    			triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    	return triangle[rowIndex]