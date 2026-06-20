class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_dict = {}
        for i in range(0,len(nums)):
            number_dict[nums[i]] = i
        for i in range(0,len(nums)):
            difference = target - nums[i]
            #key in dict
            if difference in number_dict and number_dict[difference] != i:
                return [i, number_dict[difference]]

        