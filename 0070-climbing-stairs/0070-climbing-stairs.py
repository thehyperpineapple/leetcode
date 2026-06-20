class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #base case
        if n==1 or n==0:
            return 1
        dp = [0] * (n+1)
        dp[0], dp[1] = 1,1

        # recurrence 
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
        