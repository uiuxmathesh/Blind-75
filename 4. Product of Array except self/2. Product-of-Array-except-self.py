class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod = [1]
        prefix = nums[0] * prod[0]
        for i in range(1, len(nums)):
            prod.append(prefix)
            prefix = prod[i] * nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            prod[i] = postfix * prod[i]
            postfix = postfix * nums[i]

        return prod
