class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        currMin , currMax = 1,1

        for n in nums:
            temp = currMin * n
            currMin = min(n, n * currMin, n * currMax)
            currMax = max(n, temp, n * currMax)

            res = max(res, currMax)
        
        return res