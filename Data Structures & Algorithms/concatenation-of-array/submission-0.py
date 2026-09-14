class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*(2*n)
        for ind in range(n):
            ans[ind] = nums[ind]
            ans[ind + n ] = nums[ind]
        return ans
        