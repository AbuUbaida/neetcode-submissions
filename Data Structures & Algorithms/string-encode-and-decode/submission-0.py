class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""

        for s in strs:
            inter_s = str(len(s))+'#'+s
            encoded_s+=inter_s

        return encoded_s

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        idx = 0

        while idx < len(s):
            inter_str = ""
            if s[idx]=='#':
                len_str = int(inter_str)
                str_start = idx+1
                str_end = str_start+len_str
                decoded_list.append(s[str_start:str_end+1])
                idx += len_str
            else:
                inter_str +=s [idx]
                idx += 1

        return decoded_list

