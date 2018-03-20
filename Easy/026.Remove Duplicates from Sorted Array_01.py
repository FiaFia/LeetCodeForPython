def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            print ('Current i is %s and nums[i] is %s' % (i,nums[i]))
            print ('Current j is %s and nums[j] is %s' % (j,nums[j]))
            i += 1
            print ('i is become %s' % i)
    print('Current Total Array is %s after processed' % nums)
    print('The Array after remove Duplicate is %s' % nums[:i+1])
    return i + 1

removeDuplicates([1,2,2,3,3,3,4])
