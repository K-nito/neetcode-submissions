class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}

        for i in range(len(nums)):
            x[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in x and x[difference] != i:
                return [i,x[difference]]

        return -1