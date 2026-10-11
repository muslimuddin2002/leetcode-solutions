class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Use XOR operator to find the extra character
        result = 0
        for char in s + t:
            result ^= ord(char)
        return chr(result)
