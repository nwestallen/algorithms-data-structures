# def two_sum(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i == j:
#                 continue
#             if nums[i] + nums[j] == 0:
#                 return True
#     return False

# def two_sum(nums):
#     for i, itm1 in enumerate(nums):
#         for j, itm2 in enumerate(nums):
#             if i == j:
#                 continue
#             if itm1 + itm2 == 0:
#                 return True
#     return False

# hashset solution
from collections import defaultdict
def two_sum(nums):
    # go through every element and add it to the hashset
    occurrence_map = defaultdict(int)

    for num in nums:
        occurrence_map[num] += 1

    # go through every element and check to see if its complement is in the set
    for num in nums:
        if -num in occurrence_map:
            if num == 0:
                if occurrence_map[0]>1:
                    return True
            else:
                return True
    return False

# # sort and binary search
# def two_sum(nums):
#     nums.sort()

#     for i, num in enumerate(nums):
#         left = 0
#         right = len(nums) - 1
#         complement = -num
#         while left <= right:
#             mid_idx = (right + left) // 2
#             if nums[mid_idx] == complement and i != mid_idx: 
#                 return True
#             elif nums[mid_idx] >= complement: 
#                 right= mid_idx - 1
#             elif nums[mid_idx] <= complement: 
#                 left = mid_idx + 1
#     return False


print(two_sum([1,2,4,2,5,91,7,-4,0]))