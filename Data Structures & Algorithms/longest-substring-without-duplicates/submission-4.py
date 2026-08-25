class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        r = 0
        l = 0
        uniq = set()

        while r < len(s):
            #add new element to set
            if s[r] not in uniq:
                uniq.add(s[r])
            #Since r gets a duplicate, increment l and remove elements from set until the duplicate on left boundary is reached
            else:
                while s[l] != s[r]:
                    uniq.remove(s[l])
                    l += 1
                l += 1
                
            maxLength = max(maxLength, r - l + 1)
            r += 1

        return maxLength