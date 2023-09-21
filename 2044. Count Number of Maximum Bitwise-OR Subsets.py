class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxor = 0
        for num in nums:
            maxor = maxor | num

        return self.helper(nums, 0, maxor, 0)

    def helper(self , nums, i, maxor, currxor):
        if currxor == maxor:
            remaining = len(nums) - i
            return 2 ** remaining

        if i == len(nums):
            return 0

        return self.helper(nums, i+1, maxor, currxor | nums[i]) + self.helper(nums, i+1, maxor, currxor)
