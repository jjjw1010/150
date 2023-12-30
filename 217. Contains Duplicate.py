class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Initution: Use a hashmap for O(1) access and O(1) insert
        present = set()
        for num in nums:
            if num not in present:
                present.add(num)
            else: return True
        return False
        