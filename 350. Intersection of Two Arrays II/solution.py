from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Count the occurrences of each element in nums1
        count1 = Counter(nums1)
        result = []
        
        # Iterate through nums2 and check if the element exists in count1 with a positive count
        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1
                
        return result
