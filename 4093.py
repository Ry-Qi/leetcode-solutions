
# 给你一个长度为 n 的整数数组 nums 和一个整数 k。

# 在一次操作中，你可以选择 nums 中的任意一个元素，并以任意顺序重新排列其十进制数字，组成一个新的整数。

# 返回在执行至多 k 次操作后，数组元素之和的最大值。



# 示例 1：

# 输入：nums = [123,45], k = 1

# 输出：366

# 解释：

# 选择 nums[0] = 123，重新排列其数字，得到 321。
# 数组变为 [321, 45]。因此，元素之和为 321 + 45 = 366。

class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        diff = []
        for n in nums:
            num_list = sorted(str(n))
            reverse_num, weight = 0, 1
            for c in num_list:
                reverse_num += weight*int(c)
                weight *= 10
            diff.append(reverse_num - n)
        diff.sort(reverse=True)

        return sum(nums) + sum(diff[:k])
