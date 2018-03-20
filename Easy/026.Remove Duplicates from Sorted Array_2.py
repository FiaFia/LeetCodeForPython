def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    print('The array is %s before remove duplicate item is and length is %s' % (nums,len(nums)))
    if len(nums) == 0:
        return 0

    temp = nums[0] 
    j = 1
    while j != len(nums): #不用for j in range(len(nums)):
        if nums[j] == temp:
            nums.pop(j)
        else:
            temp = nums[j]
            j += 1
    print('The array is %s after remove duplicate items and length is %s' % (nums,len(nums)))
    return len(nums)

removeDuplicates([3,5,5,5,7,7,10])
