class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second-to-last row and move upwards to the top
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the current element with itself plus the minimum of the two adjacent elements below it
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
                
        # The top element now holds the minimum path sum
        return triangle[0][0]
