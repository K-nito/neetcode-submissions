class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 

        res = []       

        i = 0      

        #iterate through list until nums[i] isn't negative
        while i < len(nums):     
            a = nums[i]
            if a > 0: 
                break

            #if current nums[i] is a duplicate, skip
            if i > 0 and a == nums[i - 1]:
                i += 1
                continue

            #create the left and right pointers
            l = i + 1
            r = len(nums) - 1

            #iterate through numbers to the right of nums[i] as long as left index is lesser than right index
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    #Skip duplicates at the left pointer
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

            i += 1

        return res

