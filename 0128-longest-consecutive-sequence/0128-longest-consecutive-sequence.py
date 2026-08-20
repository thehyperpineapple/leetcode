class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        map = set(nums)
        max_streak = 1
        for num in map:
            if (num-1) not in map:
                current = num
                count = 1
                while (current+1) in map:
                    count += 1
                    current += 1
                    max_streak = max(max_streak, count)
        return max_streak