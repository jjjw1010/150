class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Optimal Solution
        # Run time ~O(2n) -> O(n)
        # Space O(n)
        uniq = set(nums)
        longest = 0
        if len(nums) == 0 : return 0

        # Check if num is smallest then iterate
        for num in uniq:
            # ensure num is starting node
            if (num - 1) not in uniq:
                length = 1
                # iterate through the entire node
                while (num + length) in uniq:
                    length += 1
                longest = max(longest, length)
        return longest
    
        # # Brute Force O(n^2) run time O(n) space
        # n = len(nums)
        # uniq = set(nums)
        # longest = 0
        # if n == 0: return 0

        # # Locate smallest
        # smallest = nums[0]
        # for num in nums:
        #     smallest = num
        #     for ele in uniq:
        #         if ele < smallest:
        #             smallest = ele
            
        #     if smallest not in uniq:
        #         continue
                
        #     tmp = 0
        #     while smallest in uniq:
        #         uniq.remove(smallest)
        #         tmp += 1
        #         smallest += 1
        #     if longest < tmp: longest = tmp
        # return longest 

            

            
            

                    
            
