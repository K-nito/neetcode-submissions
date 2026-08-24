class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0               #left pointer
        j = len(s) - 1      #right pointer

        while i < len(s) // 2 and j >= len(s) // 2:  #Loop until any ptr hits middle
            if not s[i].isalnum():  #if left ptr isn't alnum shift right
                i += 1
                continue
            if not s[j].isalnum():  #if right ptr isn't alnum shift left
                j -= 1
                continue
            if s[i].lower() != s[j].lower():    #return False if inequal chars
                return False
            
            i += 1
            j -= 1

        return True