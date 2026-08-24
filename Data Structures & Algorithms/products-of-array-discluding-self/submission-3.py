class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create prefix array
        prefixArr = []
        prefixArr.append(1)
        i = 1
        previousProd = nums[0]

        while i < len(nums):
            prefixArr.append(previousProd)
            previousProd *= nums[i]
            i += 1

        #create suffix array
        suffixArr = []
        suffixArr.append(1)
        i = len(nums) - 2
        previousProd = nums[len(nums)-1]

        while i >= 0:
            suffixArr.append(previousProd)
            previousProd *= nums[i]
            i -= 1

        suffixArr = suffixArr[::-1]

        #create output array
        output = []

        for i in range(len(nums)):
            output.append(prefixArr[i] * suffixArr[i])

        return output
