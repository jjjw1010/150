class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) runtime
        # O(n) space

        # # [left_arr][i][right_arr]
        # # left_arr * right_arr = product of i
        # n = len(nums)

        # left_prod =  [1 for _ in range(n)]
        # right_prod = [1 for _ in range(n)]
        # prod = [1 for _ in range(n)]

        # for i in range(1, n):
        #     left_prod[i] = left_prod[i-1] * nums[i-1]
        # for j in range(n - 2, -1, -1):

        #     right_prod[j] = right_prod[j + 1] * nums[j + 1]
        # for k in range(n):
        #     prod[k] = left_prod[k] * right_prod[k]
        # return prod

        # O(n) runtime
        # O(1) Space complexity (ignore output arr prod)
        n = len(nums)
        prefix, postfix, prod= 1, 1, [1 for _ in range(n)]
        for i in range(n):
            prod[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1, -1, -1):
            prod[i] *= postfix
            postfix *= nums[i]
        return prod



