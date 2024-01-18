class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}

        # Base Case
        cache[1] = 1
        cache[2] = 2

        # To get to step n it would be
        # all step n - 1 (all climbing ways of step n - 1 is added 1)and
        # all step n - 2 (all climbing ways of step n - 2 is added 2)
        
        for i in range(3, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]