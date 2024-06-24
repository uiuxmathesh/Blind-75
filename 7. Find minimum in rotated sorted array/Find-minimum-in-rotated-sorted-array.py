class Solution:
    def findMin(self, nums: list[int]) -> int:
        end = len(nums)-1
        minimum = nums[0]

        for i in range(0,len(nums)):
            if nums[i] > nums[end]:
                i += 1
            else:
                break
            
        
        return nums[i]
            

        