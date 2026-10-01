class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        res = []
        prefix = 1
        for i in range(len(nums)):
            left[i] = prefix 
            prefix *= nums[i]
        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            right[j] = suffix
            suffix *= nums[j]
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        return res