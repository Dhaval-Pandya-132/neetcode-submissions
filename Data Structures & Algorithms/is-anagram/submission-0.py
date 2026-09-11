class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## space complexity s + t and time comlexity nlogn
        s1 = "".join(sorted(s))
        s2 = "".join(sorted(t))
        return s1 == s2
        