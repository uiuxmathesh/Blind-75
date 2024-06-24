
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maximum = -inf
        current_maximum = 0
        
        for num in nums:
            current_maximum += num
            if maximum < current_maximum:
                maximum = current_maximum
            if current_maximum < 0:
                current_maximum = 0
    
        return maximum