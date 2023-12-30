class NumArray(object):
    #Initution: Initially a left_sum array that already calculates the incremental sum of
    #the left portion of index left and left portion of index right
    #That way to find the range between index left and index right you would just do 
    #(left_sum[right] - left_sum[left] + nums[right])
    # You add nums[right] because it is not part of left_sum[right]
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.int_arr = nums
        self.len_arr = len(nums)
        self.left_sum = [0 for _ in range(self.len_arr)]    
        for i in range(1, self.len_arr):
            self.left_sum[i] = self.left_sum[i - 1] + self.int_arr[i - 1]
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.int_arr[right] + self.left_sum[right] - self.left_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)