class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for s in strs:
            ch = [0] * 26
            for c in s:
                ch[ord(c)- ord('a')] += 1
            if tuple(ch) in res:
               res[tuple(ch)].append(s) 
            else:
                res[tuple(ch)] = [s]
        return list(res.values())
