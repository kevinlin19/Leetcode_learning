def majorityElement(self, nums: List[int]) -> int:
    # nums.sort()
    # return nums[int(len(nums)/2)]
    
    # d = {}
    # d = d.fromkeys(set(nums), 0)
    # for i in nums:
    #     d[i] += 1
    #     if d[i] >= len(nums)/2:
    #         return i
    
    for i in set(nums):
        if nums.count(i) >= len(nums)/2:
            return i