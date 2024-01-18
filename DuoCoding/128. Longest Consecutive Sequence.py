class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0
        for num in numSet:
            # Look for the Base Number of Seq
            if num - 1 in numSet:
                continue

            # After you find Base Number of Seq
            # Find length of sequence
            count = 1
            while num + 1 in numSet:
                num += 1
                count += 1
            longest = max(longest, count)
        return longest