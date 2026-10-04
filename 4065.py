# No. 4065 （contest）

# 给你一个整数数组 nums。

# 初始时，你有一个 空 数组 ans。重复执行以下操作，直到 nums 变为 空 ：

# 找出当前 nums 中 所有不同 的值。
# 将当前 nums 中每个 不同 的值各移除一个，并按 升序 将这些值依次添加到 ans 中。
# 返回数组 ans。

# 示例 1：

# 输入： nums = [3,1,3,2,1,3]

# 输出： [1,2,3,1,3,3]

# 解释：

# 操作	添加到 ans 的值	操作后的 nums	操作后的 ans
# 1	1, 2, 3	[3, 1, 3]	[1, 2, 3]
# 2	1, 3	[3]	[1, 2, 3, 1, 3]
# 3	3	[]	[1, 2, 3, 1, 3, 3]
# 此时 nums 已为空，因此答案为 [1, 2, 3, 1, 3, 3]。

# 示例 2：

# 输入： nums = [7,7,4,4,4]

# 输出： [4,7,4,7,4]

# 解释：

# 操作	添加到 ans 的值	操作后的 nums	操作后的 ans
# 1	4, 7	[7, 4, 4]	[4, 7]
# 2	4, 7	[4]	[4, 7, 4, 7]
# 3	4	[]	[4, 7, 4, 7, 4]
# 此时 nums 已为空，因此答案为 [4, 7, 4, 7, 4]。



# 提示：

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

from collections import Counter

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        nums_count = Counter(nums)

        valid_num = len(nums_count)
        res = []

        while valid_num:
            for n in nums_count:
                if nums_count[n]!=0:
                    res.append(n)
                    nums_count[n]-=1
                    if nums_count[n]==0:
                        valid_num-=1

        return res

    def rearrangeArray(self, nums: list[int]) -> list[int]:
        level = [[] for _ in range(101)]
        mx = max(nums)
        cnt = [0] * (mx+1)

        nums.sort()
        for n in nums:
            cnt[n] += 1
            c = cnt[n]
            level[c].append(n)

        res = []
        for part in level:
            res += part

        return res
