class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        
        for i in strs:
            encoded_str += str(len(i)) + "#" + i

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        while i < len(s):
            length = 0

            #read length
            while s[i] != "#":
                length = length * 10 + int(s[i])
                i += 1
            
            #skip hash
            i += 1 

            #read word
            decoded_str.append(s[i:i+length])
            i += length

        return decoded_str