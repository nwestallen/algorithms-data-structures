#https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged = []
        i = 0
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
                
        if j == len(nums2):
            while i < len(nums1):
                merged.append(nums1[i])
                i += 1
        else:
            while j < len(nums2):
                merged.append(nums2[j])
                j += 1
        
        mlen = len(merged)
        if mlen % 2 != 0:
            return merged[mlen//2]
        else:
            return (merged[mlen//2] + merged[mlen//2 - 1])/2

def test_simple():
    assert Solution().findMedianSortedArrays([2,6,8], [1,3,5,7]) == 5

def test_empty_left():
    assert Solution().findMedianSortedArrays([], [3,4,5]) == 4