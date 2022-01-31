class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)-1):
            try:
                j = numbers[i+1:].index(target-numbers[i])
                return [i+1,j+1+i+1]

            except:
                continue