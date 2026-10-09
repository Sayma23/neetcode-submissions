class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        prevTime = (target - pair[0][0])/ pair[0][1]
        fleet = 1
        for i in range(1, len(pair)):
            curTime = (target - pair[i][0])/ pair[i][1]
            if (curTime > prevTime):
                fleet += 1
                prevTime = curTime
        return fleet
        