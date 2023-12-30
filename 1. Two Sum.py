class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Initution: Use hash_map for O(1) access so runtime is O(n) not O(n^2)
        # 1) Iterate through nums
        # 2) Find complementary of num
        # 3) Check if it exists in hash_map (key (num value): value: (num index))
        # 4) If it does, return the index of comp and current i iteration value
        # 5) Else store num and its index i into the hash map

        num_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_map:
                return [i, num_map[comp]]
            # No need to worry about having duplicate keys
            num_map[num] = i