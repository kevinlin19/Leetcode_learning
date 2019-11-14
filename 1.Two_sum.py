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

