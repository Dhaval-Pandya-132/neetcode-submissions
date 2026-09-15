class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
       # print(nums)
        start = 0 
        result = dict()
        while start < len(nums)-1:
            left = start +1 
            right = len(nums) -1
            while left < right:
                #print(f"{nums[start]}#{nums[left]}#{nums[right]}")
                if nums[start] + nums[left] + nums[right] >0 :
                    right -=1
                elif  nums[start] + nums[left] + nums[right] < 0 :
                    left +=1
                else:
                    key = f"{nums[start]}#{nums[left]}#{nums[right]}"
                    result[key]= [nums[start],nums[left],nums[right]]
                    right -=1
                    left +=1

            start +=1 
        return list(result.values())