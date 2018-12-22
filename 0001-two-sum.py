class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        search_table = {}        
        for index, num in enumerate(nums):
            try:
                return [index, search_table[target - num]]
            except KeyError:
                search_table[num] = index
