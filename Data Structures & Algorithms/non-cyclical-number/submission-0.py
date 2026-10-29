class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while n != 1:
            sum_ = self.summary(n)
            if sum_ in seen:
                return False
            seen.append(sum_)
            n = sum_
        return True

    def summary (self, n: int) -> int:
        sum_ = 0
        while n//10 > 0:
            rem = n % 10
            sum_ += rem * rem
            n = n//10
        sum_ += n * n
        print(sum_)
        return sum_