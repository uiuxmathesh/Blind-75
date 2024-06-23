class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for i, num in enumerate(nums):
            nums[i] = [num, i]
        
        nums.sort()

        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i][0] + nums[j][0] == target:
                idx1 = nums[i][1]
                idx2 = nums[j][1]
                return [idx1, idx2]
            elif nums[i][0] + nums[j][0] < target:
                i+=1
            elif nums[i][0] + nums[j][0] > target:
                j-=1
        
        return []


        