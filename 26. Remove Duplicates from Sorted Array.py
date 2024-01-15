class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initution: This is a Two Pointer Question
        # One pointer that iterates through each number
        # One pointer that writes over the array at the instance of a new value
        # We use set to keep track of which number was used
        n = len(nums)
        write = 0
        used = set()
        for i in range(n):
            if nums[i] not in used:
                nums[write] = nums[i]
                used.add(nums[i])
                write += 1
        return write