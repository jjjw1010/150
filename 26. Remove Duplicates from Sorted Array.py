class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initution: This is a Two Pointer Question
        # One pointer that iterates through each number (Fast Pointer)
        # One pointer that writes over the array at the instance of a new value (Slow Pointer)
        # Done in O(1) space complexity
        
        slow = 0 # nums[slow] = nums[0]
        for fast in range(1, len(nums)):
            # Find when fast value is different from slow value
            if nums[slow] != nums[fast]:
                # Set next slow value to the different fast value 
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
        
        # Diff Approach
        # We can also do it in O(n) Space Complexity
        # We use set to keep track of which number was used
        
        # n = len(nums)
        # write = 0
        # used = set()
        # for i in range(n):
        #     if nums[i] not in used:
        #         nums[write] = nums[i]
        #         used.add(nums[i])
        #         write += 1
        # return write