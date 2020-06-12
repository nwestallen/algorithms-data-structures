class Solution:
    def rob(nums):
        l1 = [j for i, j in enumerate(nums) if i % 2 != 0]
        l2 = [j for i, j in enumerate(nums) if i % 2 == 0]
        return max(sum(l1), sum(l2))


my_nums = [1, 2, 3, 4, 2, 100]

print(Solution.rob(my_nums))
