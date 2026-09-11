class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in index_map:
                return [index_map.get(diff), index]
            index_map[num] = index
        return []
        ### Time complexity O(n) & Space Complexity O(N)