class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        UniqueNums = []

        for i in nums:
            if i not in UniqueNums:
                UniqueNums.append(i)
            else:
                return True

        return False
