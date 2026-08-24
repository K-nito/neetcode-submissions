class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashSet = set(nums)

        seqDict = {}

        i = 0

        while i < len(nums):
            if (nums[i] - 1) not in hashSet:
                seqStart = nums[i]
                seqDict[seqStart] = [seqStart]
                j = 1
                while (nums[i] + j) in hashSet:
                    seqDict[seqStart].append(nums[i] + j)
                    j += 1
            i += 1

        maxLen = max(len(seq) for seq in seqDict.values())

        return maxLen
