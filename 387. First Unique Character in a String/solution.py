from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        # Iterate through the string to find the first character with a count of 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
                
        return -1
