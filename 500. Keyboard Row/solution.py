class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        for word in words:
            # Convert word to lowercase for case-insensitive comparison
            w_lower = word.lower()
            char_set = set(w_lower)
            
            # Check if all characters of the word belong to any single row
            if char_set.issubset(row1) or char_set.issubset(row2) or char_set.issubset(row3):
                result.append(word)
                
        return result
