class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_dict = {}
        for num in nums:
            number_dict[num] = 1 + number_dict.get(num, 0)
        output_dict = dict(sorted(number_dict.items(), key=lambda item:item[1], reverse=True))
        return list(output_dict)[:k]