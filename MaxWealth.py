"""
Leetcode #1672 : You are given an m x n integer grid accounts where accounts[i][j] is the amount of money 
the ith customer has in the jth bank. Return the wealth that the richest customer has
A customer's wealth is the amount of money they have in all their bank accounts
The richest customer is the customer that has the maximum wealth

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

Example 2:
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10

Example 3:
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum1 = maxW = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                sum1 = sum1 + accounts[i][j]
            maxW = max(sum1, maxW)
            sum1 = 0
        return maxW