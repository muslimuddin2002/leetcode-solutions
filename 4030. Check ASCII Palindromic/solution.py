class Solution:
    def isPalindromic(self, s: str) -> bool:
    
        binary_str = "".join(format(ord(c), '08b') for c in s)
        
        
        return binary_str == binary_str[::-1]
