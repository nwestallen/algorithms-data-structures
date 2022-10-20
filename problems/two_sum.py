from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(nums)):
            if target - nums[i] in complements:
                return [complements[target - nums[i]], i]
            else:
                complements[nums[i]] = i

def test_two_sum_1():
    nums = [2, 7, 11, 15]
    target = 9
    assert Solution().twoSum(nums, target) == [0, 1]

def test_two_sum_2():
    nums = [3, 2, 4]
    target = 6
    assert Solution().twoSum(nums, target) == [1, 2]

def test_two_sum_3():
    nums = [3, 3]
    target = 6
    assert Solution().twoSum(nums, target) == [0, 1]