class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        no_zeros = 0

        for i in range(len(nums)):
            if nums[i]:
                nums[no_zeros],nums[i] = nums[i],nums[no_zeros]
                no_zeros += 1