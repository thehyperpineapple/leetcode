class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        checking_dict = {}
        for value in nums:
            if value in checking_dict:
                return True
            else:
                checking_dict[value] = 1
        return False