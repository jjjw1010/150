class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initution: Since the place is arranged in a circle, you know
        # for sure you can't rob 1st house and last house
        # Thus, you would use function from House Robber I and return
        # max(rob([0:n]),rob([1:n-1]))
        n = len(nums)

        #Base Case
        if n <= 3: return max(nums)

        def rob(nums):
            n = len(nums)
            if n <= 2: return max(nums)
            cache = {}
            n = len(nums)
            cache[0] = nums[0]
            cache[1] = nums[1]
            cache[2] = nums[0] + nums[2]

            for i in range(3, n):
                cache[i] = max(cache[i - 2], cache[i - 3]) + nums[i]

            return max(cache[n-1], cache[n-2])
        return max(rob(nums[1:n]), rob(nums[0:n-1]))