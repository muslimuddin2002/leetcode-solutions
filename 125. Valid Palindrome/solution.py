class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter the string to keep only alphanumeric characters and convert to lowercase
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        # Check if the filtered list reads the same forwards and backwards
        return filtered_chars == filtered_chars[::-1]
