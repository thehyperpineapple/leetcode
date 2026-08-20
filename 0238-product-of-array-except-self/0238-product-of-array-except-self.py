class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1]*len(nums)
        suffix_array = [1]*len(nums)
        output_array = [1]*len(nums)
        prefix_product = 1
        suffix_product = 1
        for i in range(0,len(nums)):
            prefix_product = prefix_product*nums[i]
            suffix_product = suffix_product*nums[len(nums)-1-i]

            prefix_array[i] = prefix_product
            suffix_array[len(nums)-1-i] = suffix_product

        for i in range(0,len(nums)):
            if i == 0:
                output_array[i] = 1 * suffix_array[i+1]
            elif i == len(nums)-1:
                output_array[i] = 1 * prefix_array[i-1]
            else:
                output_array[i] = prefix_array[i-1]*suffix_array[i+1]

        return output_array