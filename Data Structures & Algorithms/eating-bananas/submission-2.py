class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_count = max (piles)
        min_count = 1
        valid_speed = max_count
        while min_count <= max_count:
            mid = (max_count + min_count) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(float(piles[i])/mid)
            if (hours > h):
                min_count = mid + 1
            else:
                valid_speed = mid
                max_count = mid - 1
        return valid_speed