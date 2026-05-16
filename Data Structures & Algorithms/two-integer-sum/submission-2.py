class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_idx = {}
        for i in range(0,len(nums)):
            to_comp = target-nums[i]
            if to_comp in dict_idx:
                return [dict_idx[to_comp], i]
            else:
                dict_idx[nums[i]] = i
        