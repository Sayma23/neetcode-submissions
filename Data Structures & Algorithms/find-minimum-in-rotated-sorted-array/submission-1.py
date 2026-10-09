class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            left, right = mid - 1, mid + 1
            if(mid-1 < 0):
                left = len(nums) -1
            if (mid + 1 == len(nums)):
                right = 0
            if(nums[mid] < nums[left] and nums[mid] < nums[right]):
                return nums[mid]
            elif (nums[mid] < nums[r]):
                r = mid - 1
            else:
                l = mid + 1
        return nums[0]

        