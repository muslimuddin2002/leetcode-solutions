# Time Complexity: O(n) - single pass through the array
# Space Complexity: O(1) - modifies the array in-place, no extra space used

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
