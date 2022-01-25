class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 2:
            return [0,1]
        
        p = 0
        
        while p < len(nums)-1:
             
            if target - nums[p] in nums[p+1:]:
                return [p,nums[p+1:].index(target - nums[p])+p+1]
                    
            p += 1
        
        return [p,len(nums)-1]
            
            
        