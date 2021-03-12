"""
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。



示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [0]
输出：0
示例 4：

输入：nums = [-1]
输出：-1
示例 5：

输入：nums = [-100000]
输出：-100000


提示：

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105


进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

通过次数423,309提交次数793,124
"""
from typing import List


class Solution:
    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        # dp = [nums[0]]
        pre = nums[0]
        ans = nums[0]
        for i in range(len(nums)):
            if i > 0:
                # dp.append(max(nums[i], dp[i - 1] + nums[i]))
                pre = max(nums[i], pre + nums[i])
                ans = max(ans, pre)
        return ans


print(Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
