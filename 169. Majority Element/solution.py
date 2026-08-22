class Solution:
    # Time: O(n) - single pass through nums
    # Space: O(1) - only two variables used
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
