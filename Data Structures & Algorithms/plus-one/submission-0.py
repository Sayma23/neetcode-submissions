class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        index = len(digits) - 1
        carry = 1
        while index >= 0:
            total = carry + digits[index]
            output.append(total%10)
            carry = total//10
            index -= 1
        if carry > 0:
            output.append(carry)
        output.reverse()
        return output
        