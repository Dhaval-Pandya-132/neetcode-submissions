class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ### Brute force O(n^2)
        # result = []
        # for index in range(len(nums)):
        #     multi = 1
        #     for index_2 in range(len(nums)):
        #         if index != index_2:
        #             multi *=nums[index_2]
        #     result.append(multi)
        # return result 

        ### Hint Prefix and post fix array 
        ### NOTE: Make sure you build the prefix and post fix arra coorectly 
        ### Visualize the prefix and post fix arran and based on that write logic 
        n = len(nums)
        prefix = [0]*n
        postfix = [0]*n
        result = [0]*n
        prefix[0] = postfix[n-1] = 1
        for index in range(1,n):
            prefix[index] = prefix[index-1]* nums[index-1] 

        for index in range(n-2,-1,-1):
            postfix[index] = postfix[index+1] * nums[index+1]
 
        for index in range(n):
            result[index] = prefix[index] * postfix[index]
        return result
        
