class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return max(nums)
        cache = {}
        n = len(nums)
        cache[0] = nums[0]
        cache[1] = nums[1]
        cache[2] = nums[0] + nums[2]

        for i in range(3, n):
            cache[i] = max(cache[i - 2], cache[i - 3]) + nums[i]

        return max(cache[n-1], cache[n-2])