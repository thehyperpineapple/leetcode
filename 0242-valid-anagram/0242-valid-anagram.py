class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        s_dict, t_dict = {}, {}
        for letter in len(s):
            s_dict[i] = 1 + s_dict.get(s[i], 0)
            t_dict[i] = 1 + t_dict.get(t[i], 0)
        if s_dict == t_dict:
            return True
        else:
            return False