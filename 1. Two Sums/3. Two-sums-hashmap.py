class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        found_pairs = {}
        for i in range(0, len(nums)):
            needed_number = target-nums[i]
            needed_index = found_pairs.get(needed_number, None)
            if needed_index != None:
                return[i, needed_index] 
            else:
                found_pairs.update({nums[i]: i})