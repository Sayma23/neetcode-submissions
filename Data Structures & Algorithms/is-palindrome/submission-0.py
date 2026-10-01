class Solution:
    def isPalindrome(self, s: str) -> bool:
        limit = 0
        s = s.lower()
        cleaned = "".join(c for c in s if c.isalnum())
        print(cleaned)
        if (len(cleaned) % 2 == 0 ):
            limit = len(cleaned) / 2
        else: 
            limit = int(len(cleaned) / 2) + 1
        for i in range(int(limit)):
            print(cleaned[i])
            print(cleaned[len(cleaned)-i-1])
            if(cleaned[i] != cleaned[len(cleaned)-i-1]):
                return False
        return True