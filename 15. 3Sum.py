class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Initution: This is a Two Pointer Problem
        # We can fixated one value and use the approach when solving Two Sum Sorted Array
        # with each fixated value acting as the target value
        # This would take O(nlogn) + O(n) * O(n) = O(n^2) time with O(n) space complexity

        ans = []
        nums.sort() # To use Two Pointers need sorted Array
        n = len(nums)
        for i in range(n):
            # we already did a case for nums[i]
            # skip to the next unique nums[i] value
            if i > 0 and nums[i] == nums[i - 1]: continue

            target = -1 * nums[i]
            left, right = i + 1, n - 1
            while(right > left):
                if target < nums[left] + nums[right]: 
                    right -= 1
                elif target > nums[left] + nums[right]: 
                    left += 1
                else:
                    # on target!
                    ans.append([nums[i], nums[left], nums[right]]) 
                    left += 1

                    # We already appended the case for nums[left] value
                    # Move on to the next different nums[left] value
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return ans
