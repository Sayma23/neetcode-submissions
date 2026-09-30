class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = dict()
        for i in range(len(nums)):
            if(pair.get(nums[i]) != None):
                return [pair.get(nums[i]), i]
            else:
                pair[target - nums[i]]= i
        return []