class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lenght = len(nums)

        if k >= lenght:
            k -= lenght

        if k == 0:
            return
        nums[:k],nums[k:] = nums[lenght-k:],nums[:lenght-k]