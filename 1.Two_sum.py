# First Solution
import numpy as np
class Solution:
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            left = target - nums[i]
            candidate = np.where(np.array(nums) == left)[0].tolist()
            if (len(candidate) >= 1):
                if (candidate[-1] != i):
                    return [i, candidate[-1]]

    # Second Solution
    def twoSum_second(self, nums, target):
        """
        :type num: list[int]
        :type target: int
        ::type return: list[int]
        """
        hash_table = dict()
        
        for idx, num in enumerate(nums):
            left = target - num
            if left not in hash_table:
                hash_table[num] = idx
            else:
                return [hash_table[left], idx]



