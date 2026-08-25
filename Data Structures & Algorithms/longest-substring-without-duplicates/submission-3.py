class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        r = 0
        l = 0
        uniq = set()

        while r < len(s):
            if s[r] not in uniq:
                uniq.add(s[r])
            else:
                while s[l] != s[r]:
                    uniq.remove(s[l])
                    l += 1
                l += 1
                
            maxLength = max(maxLength, r - l + 1)
            r += 1

        return maxLength