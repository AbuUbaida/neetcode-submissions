from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
        
        print(list(sorted_d)[:k])
