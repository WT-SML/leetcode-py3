"""
1052. 爱生气的书店老板
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意的数量。


示例：

输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.


提示：

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
通过次数15,706提交次数27,806
"""
from typing import List


class Solution:
    @staticmethod
    def maxSatisfied(customers: List[int], grumpy: List[int], X: int) -> int:
        # 滑动窗口
        s = 0  # 不使用技能时的满意顾客
        ic_max = 0  # 发动技能获取的满意顾客收益
        c = 0  # 缓存滑动窗口内的和
        # 统计不使用技能时的满意顾客
        for i in range(len(customers)):
            if grumpy[i] == 0:
                s += customers[i]
                customers[i] = 0  # 将已统计过的顾客归0
        # 统计发动技能获取的满意顾客收益
        for i in range(len(customers) - X + 1):
            if i == 0:
                c = sum(customers[:i + X])
            else:
                c = c - customers[i - 1] + customers[i + X - 1]
            ic_max = max(c, ic_max)
        return s + ic_max


print(Solution.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
