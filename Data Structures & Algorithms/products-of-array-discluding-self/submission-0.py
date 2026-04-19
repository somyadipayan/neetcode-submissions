class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)

        # Prefix products
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Postfix products
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res