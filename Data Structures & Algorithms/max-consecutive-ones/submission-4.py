class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = current = 0
        for num in nums :
            if num == 0:
                current = 0
                continue
            current +=1
            result = max(result, current)
        return result 