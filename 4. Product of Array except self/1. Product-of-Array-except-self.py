class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre_prod = [*nums]
        post_prod = [*nums]
        pre_prod[0] = 1
        post_prod[-1] = 1
        
        for i in range(1, len(nums)):
            pre_prod[i] = pre_prod[i-1] * nums[i-1]

        print(pre_prod)

        for i in range(len(nums)-2, -1, -1):
            post_prod[i] = post_prod[i+1] * nums[i+1]

        print(post_prod)
        
        for i in range(0, len(nums)):
            nums[i] = pre_prod[i] * post_prod[i]
            
        
        print(nums)

        return nums
