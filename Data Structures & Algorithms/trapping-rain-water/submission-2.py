class Solution:
    def trap(self, height: List[int]) -> int:
        #Create prefix array
        preMax = 0
        pMaxArr = []
        i = 0

        while i < len(height):
            i += 1
            pMaxArr.append(preMax)
            preMax = max(preMax, height[i - 1])

        #Create suffix array
        sufMax = 0
        sMaxArr = []
        i = len(height) - 1

        while i >= 0:
            i -= 1
            sMaxArr.append(sufMax)
            sufMax = max(sufMax, height[i + 1])

        #Reverse to get correct positions, as we iterated from end to start
        sMaxArr = sMaxArr[::-1]

        res = 0

        #iterate through given array, calculating water at each index and summing up
        for i in range(len(height)):
            water = min(pMaxArr[i], sMaxArr[i]) - height[i]
            res += max(water, 0)

        return res 

                