class Solution:
    def twoSum(self, nums, target):
        """
        思路：不用排序
        如果存在着一对解m, n，设m在序列中排在n的前面。
        我们从头到尾遍历该序列，用数据结构S存储已经遍历过的数据。
        遍历到m时候，寻找target-m是否在S中，这时候还是不在。
        但是遍历到n的时候就发现target-n，也就是m，在S中
        """
        tmp_nums = {}
        for i in range(len(nums)):
            if target - nums[i] in tmp_nums:
                return (tmp_nums[target -nums[i]], i)
            else:
                tmp_nums[nums[i]] = i
        return (-1, -1)
