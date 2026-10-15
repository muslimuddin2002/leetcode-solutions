class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
            
        # Handle negative numbers using two's complement for a 32-bit integer
        if num < 0:
            num += 2**32
            
        hex_chars = "0123456789abcdef"
        result = []
        
        while num > 0:
            remainder = num % 16
            result.append(hex_chars[remainder])
            num //= 16
            
        return "".join(result[::-1])
