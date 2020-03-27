# -*- coding: utf-8 -*-
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# https://leetcode-cn.com/problems/climbing-stairs


class Solution70:
    @staticmethod
    def climb_stairs(n: int) -> int:
        if n < 3:
            return n
        # climb 1 or 2 stairs
        dp1, dp2 = 1, 2
        ans = 0
        for _ in range(3, n + 1):
            # each step is the sum of previous steps
            ans = dp1 + dp2
            dp1, dp2 = dp2, ans
        return ans
