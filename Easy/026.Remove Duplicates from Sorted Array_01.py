'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length. 

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

ExampleGiven nums = [1,1,2],Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the new length.
'''

'''
方法一
数组是有序的，设置两个指针i和j，都从nums[0]开始，j用for循环依次往后走，比较nums[j]与 nums[i]的值，
当nums[i]与nums[j]值相等时，j往后走一步，j + 1；
当nums[i]的值与nums[j]的值不相等时，把nums[j]的值放到nums[i]后面的位置，即nums[i+1],i往后走1步
这样只要返回nums[0:i+1] 即是删除重复项的数组
'''
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

'''
方法二
因为是有序数组，重复的元素一定是相邻的，不用单独记录
设置一个临时变量，用它来和后面的数值进行比较，如果相同，就把对应的nums[j]删除，
用while而不用for 循环，是因为会pop会导致数组长度变化，可能会引起list index out of range error
'''
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
