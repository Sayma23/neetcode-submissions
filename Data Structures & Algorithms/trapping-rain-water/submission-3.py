class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]
        for i in range (1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i-1])
        for i in range (len(height) - 2, -1, -1):
            rightMax[i] = max (rightMax[i+1], height[i+1])
        
        for i in range(len(height)):
            totalWater += 0 if (min (leftMax[i], rightMax[i]) - height[i]) < 0 else min (leftMax[i], rightMax[i]) - height[i]
        return totalWater
        