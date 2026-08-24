class Solution:
    def trap(self, height: List[int]) -> int:
        preMax = 0
        pMaxArr = []
        i = 0

        while i < len(height):
            i += 1
            pMaxArr.append(preMax)
            preMax = max(preMax, height[i - 1])

        sufMax = 0
        sMaxArr = []
        i = len(height) - 1

        while i >= 0:
            i -= 1
            sMaxArr.append(sufMax)
            sufMax = max(sufMax, height[i + 1])

        sMaxArr = sMaxArr[::-1]

        res = 0

        for i in range(len(height)):
            water = min(pMaxArr[i], sMaxArr[i]) - height[i]
            res += max(water, 0)

        return res 

                