class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        previous = None
        for num in nums:
            if num == previous:
                return True
            previous = num
        
        return False