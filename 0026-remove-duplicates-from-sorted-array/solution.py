# Time Complexity: O(n) - single pass through the array
# Space Complexity: O(1) - modifies the array in-place, no extra space used

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
