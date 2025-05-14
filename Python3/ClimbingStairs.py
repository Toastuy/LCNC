# This is the most verbose solution that follows the principal the problem is trying to teach
# The most efficient solution to this problem though would use dynamic programming or math
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case is when we are a 1 or a 0, in this case both of these result
        # in one distinct way to climb the stairs
        if n == 1 or n == 0:
            return 1
        return self.climbStairs(n-2) + self.climbStairs(n-1)