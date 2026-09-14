class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        n = len(nums)
        for ind in range(n):
            if nums[ind] != val:
                nums[j] = nums[ind]
                j +=1
                
        return j 
        