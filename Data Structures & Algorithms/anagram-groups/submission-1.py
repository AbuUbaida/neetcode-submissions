from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            int_list = [0]*26

            for c in s:
                idx = ord(c)-ord('a')
                int_list[idx] += 1

            result[tuple(int_list)].append(s)

        return list(result.values())