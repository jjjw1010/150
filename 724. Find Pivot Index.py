class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initution: 
        # First have a total sum of all elements in num array.
        # Then in a loop we would decrement right_sum so that we don't include 
        # nums[i] in the right part. 
        # Then we would check if left_sum is equal to right_sum
        # If it is we would return the pivot index
        # Else we would increase left sum by current num value 
        # We would return -1 if there is no pivot index
        n = len(nums)
        left_sum = 0
        right_sum = sum(nums)
        for i in range(n):
            right_sum -= nums[i]
            if left_sum == right_sum: return i
            left_sum += nums[i]
        return -1