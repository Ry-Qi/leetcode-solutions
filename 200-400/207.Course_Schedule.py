# No.207 Course schedule
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi]
# indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0
# you should also have finished course 1. So it is impossible.

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        preCourse = defaultdict(list)
        for a, b in prerequisites:
            preCourse[a].append(b)

        cache = set()
        path = set()
        def learn(curCourse):
            if curCourse in path:
                return False

            if curCourse in cache:
                return True

            if curCourse not in preCourse or len(preCourse[curCourse])==0:
                return True

            path.add(curCourse)

            for pre in preCourse[curCourse]:
                ok = learn(pre)
                if not ok:
                    return False
            cache.add(curCourse)
            path.discard(curCourse)
            return True

        for i in range(numCourses):
            if not learn(i):
                return False

        return True

print(Solution().canFinish(2, [[1,0]]))

nums = [1,2]
nums.extend([3,4])
print(nums)
