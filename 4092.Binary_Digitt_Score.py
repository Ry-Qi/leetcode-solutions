# 给你两个整数 a 和 b。

# 设 s1 和 s2 分别为 a 和 b 的二进制表示中置位的数量。

# 这两个整数的得分定义如下：

# 如果 s1 >= s2，则得分为 s1 * s2。
# 否则，得分为 s2 / s1，其中除法采用整数除法。
# 返回一个整数，表示 a 和 b 的得分。

# 置位是指数的二进制表示中值为 1 的位。

# 示例 1：

# 输入： a = 14, b = 6

# 输出： 6

# 解释：

# a = 14 的二进制表示为 "1110"，因此 s1 = 3。
# b = 6 的二进制表示为 "110"，因此 s2 = 2。
# 由于 s1 > s2，a 和 b 的得分为 s1 * s2 = 3 * 2 = 6。


class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        tmpa, tmpb = a, b
        s1, s2 = 0, 0
        while tmpa:
            if tmpa%2==1:
                s1 +=1
            tmpa //= 2
        while tmpb:
            if tmpb%2==1:
                s2 +=1
            tmpb //= 2
        return s1*s2 if s1>=s2 else s2//s1
