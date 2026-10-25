# No. 173 点名

# 某班级 n 位同学的学号为 0 ~ n-1。点名结果记录于升序数组 records。假定仅有一位同学缺席，请返回他的学号。

# 示例 1：

# 输入：records = [0,1,2,3,5]
# 输出：4
# 示例 2：

# 输入：records = [0, 1, 2, 3, 4, 5, 6, 8]
# 输出：7


class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        l, r = 0, len(records)-1

        res = 0
        while l<=r:
            i = l + (r-l)//2
            n = records[i]

            if i==n:
                l = i + 1
            else:
                res = i
                r = i - 1
        if l==len(records):
            return l

        return res
