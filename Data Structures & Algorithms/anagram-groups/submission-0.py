class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for s in strs:
            temp = "".join(sorted(s))
            if temp in res:
               res[temp].append(s) 
            else:
                res[temp] = [s]
        return list(res.values())
