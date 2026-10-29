# 给你一个整数数组 nums。

# 考虑一个子数组中的所有不同值，并按它们首次出现的顺序排列。

# 如果其中有 k 个不同值，且第一个不同值恰好出现一次，第二个不同值恰好出现两次
# 以此类推，第 k 个不同值恰好出现 k 次，则称该子数组为频次阶梯。

# 即，按首次出现的顺序排列的各个不同值，其出现次数必须恰好为 1, 2, 3, ..., k。

# 返回 nums 中频次阶梯子数组的数量。

# 子数组是数组中一段连续且非空的元素序列。

# 一个值在子数组中的频次，是指它在该子数组中出现的次数。



# 示例 1：

# 输入：nums = [5,8,8,2,2,2]

# 输出：9

# 解释：

# 每个单元素子数组的频次序列都是 [1]，这样的子数组共有 6 个。另外还有 3 个更长的子数组符合条件：

# 子数组	按首次出现顺序排列的值	频次
# nums[0...2] = [5, 8, 8]	先 5，后 8	[1, 2]
# nums[2...4] = [8, 2, 2]	先 8，后 2	[1, 2]
# nums[0...5] = [5, 8, 8, 2, 2, 2]	依次为 5、8、2	[1, 2, 3]
# 因此，答案为 6 + 3 = 9。

from collections import defaultdict

class Solution:
    def countStaircase(self, nums: list[int]) -> int:

        res = 0
        i, j = 0, 0
        while i < len(nums):
            j = i
            count, orders = defaultdict(int), defaultdict(int)
            valid = 0
            while j < len(nums):
                r = nums[j]
                if r not in orders:
                    orders[r] = len(orders) + 1
                count[r] += 1
                if count[r] == orders[r]:
                    valid += 1
                elif count[r] > orders[r]:
                    break
                if valid == len(orders):
                    res += 1
                j += 1
            i += 1
        return res
