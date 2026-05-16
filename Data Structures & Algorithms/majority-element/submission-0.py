class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}

        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1

        sorted_list = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)

        return sorted_list[0][0]