# No. 3481 Apply Substitutions
# 题目描述
# 给定一个 replacements 映射和一个可能包含格式为 %var% 占位符 的字符串 text，其中每个 var 对应 replacements 中的一个键。
# 每个替换值本身可能包含 一个或多个 此类占位符。每个 占位符 都被与其相应的替换键对应的值替换。

# 返回完全替换后 不 含任何 占位符 的 text 字符串。



# 输入：replacements = [["A","abc"],["B","def"]], text = "%A%_%B%"
# 输出："abc_def"
# 解释：
# 映射将 "A" 与 "abc" 关联，并将 "B" 与 "def" 关联。
# 用 "abc" 替换文本中的 %A%，并用 "def" 替换文本中的 %B%。
# 最终文本变为 "abc_def"。

# 输入：replacements = [["A","bce"],["B","ace"],["C","abc%B%"]], text = "%A%_%B%_%C%"
# 输出："bce_ace_abcace"
# 解释：
# 映射将 "A" 与 "bce" 关联，"B" 与 "ace" 关联，以及 "C" 与 "abc%B%" 关联。
# 用 "bce" 替换文本中的 %A%，并用 "ace" 替换文本中的 %B%。
# 接着，对于 %C%，用 "ace" 替换 "abc%B%" 中的 %B% 来得到 "abcace"。
# 最终文本变为 "bce_ace_abcace"

from collections import defaultdict

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        replace_map = {}
        for k, v in replacements:
            replace_map[k] = v

        def dfs(k):
            if k not in replace_map:
                return ''
            value = replace_map[k]
            i = 0
            valid_value = ''
            while i < len(value):
                if value[i] == '%':
                    i += 1
                    new_key = ''
                    while value[i] != '%':
                        new_key += value[i]
                        i += 1
                    valid_value += dfs(new_key)
                else:
                    valid_value += value[i]
                i += 1
            return valid_value

        res = ''
        i = 0
        while i < len(text):
            if text[i] == '%':
                i += 1
                new_key = ''
                while text[i] != '%':
                    new_key += text[i]
                    i += 1
                res += dfs(new_key)
            else:
                res += text[i]
            i += 1
        return res

    def applySubstitutions2(self, replacements: List[List[str]], text: str) -> str:
        replace_map = {}
        for k, v in replacements:
            replace_map[k] = v

        cache = {}
        def valid_value(text):
            res = ''
            i = 0
            while i < len(text):
                if text[i] == '%':
                    i += 1
                    new_key = ''
                    while text[i] != '%':
                        new_key += text[i]
                        i += 1
                    part = None
                    if new_key in cache:
                        part = cache[new_key]
                    else:
                        part = valid_value(replace_map[new_key])
                    cache[new_key] = part
                    res += part
                else:
                    res += text[i]
                i += 1
            return res

        return valid_value(text)

s = '%afaf%fadf%fds%d%s%f%e%efe%e%%'

print(s.split('%'))
