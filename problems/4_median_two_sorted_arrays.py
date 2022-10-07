#https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List

class Solution:
    def findMedianSortedArrays_brute(self, nums1: List[int], nums2: List[int]) -> float:
        
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
    
    def median(self, numList):
        mid = len(numList) // 2 
        if len(numList) % 2 == 0:
            return (numList[mid - 1] + numList[mid]) / 2
        else:
            return numList[mid]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if not nums1:
            return self.median(nums2)
        elif not nums2:
            return self.median(nums1)
        elif self.median(nums1) == self.median(nums2):
            return self.median(nums1)
        elif self.median(nums1) > self.median(nums2):
            if len(nums2) == 1:
                return self.median(nums1[:len(nums1)//2])
            else:
                return self.findMedianSortedArrays(nums1[:len(nums1)//2], nums2[len(nums2)//2:])
        else:
            if len(nums1) == 1:
                return self.median(nums2[:len(nums2)//2])
            else:
                return self.findMedianSortedArrays(nums1[len(nums1)//2:], nums2[:len(nums2)//2])

def test_simple():
    assert Solution().findMedianSortedArrays([2,6,8], [1,3,5,7]) == 5

def test_empty_left():
    assert Solution().findMedianSortedArrays([], [3,4,5]) == 4

def test_empty_right():
    assert Solution().findMedianSortedArrays([3,6,10,11], []) == 8

def test_asymmetric_high():
    assert Solution().findMedianSortedArrays([100], [1, 2, 3, 4]) == 3

def test_asymmetric_low():
    assert Solution().findMedianSortedArrays([1, 2, 3], [0]) == 1.5

def test_between():
    assert Solution().findMedianSortedArrays([1,3,5,7], [9,12,15,18]) == 8

def test_median_odd():
    assert Solution().median([1,2,3]) == 2

def test_median_even():
    assert Solution().median([2,4,6,8]) == 5

def test_base():
    assert Solution().findMedianSortedArrays([], [1,2,3]) == 2

if __name__ == "__main__":
    test_simple()
