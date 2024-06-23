class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numsDict = {}
        for num in nums:
            if numsDict.get(num, None) == None:
                numsDict.update({num:1})
            else:
                return True
        
        return False