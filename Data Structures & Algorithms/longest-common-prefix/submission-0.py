class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""

        for i in range(len(strs[0])):
            curr_char = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or curr_char != strs[j][i]:
                    return lcp
            lcp += curr_char
        return lcp