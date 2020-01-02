def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # c = nums.count(0)
    
    # while c > 0:
    #     nums.remove(0)
    #     nums.insert(len(nums), 0)
    #     c += -1
    
    # for _ in range(c):
    #     nums.remove(0)
    #     nums.extend([0])
    
    n_zero = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[n_zero], nums[i] = nums[i], nums[n_zero]
            n_zero += 1