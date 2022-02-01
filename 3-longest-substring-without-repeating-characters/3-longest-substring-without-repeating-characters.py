class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr = 0
        left = 0
        max_len = 0
        l = []
        while ptr < len(s):

            if s[ptr] not in l:
                l.append(s[ptr])
                ptr += 1
            else:
                if len(l) > max_len:
                    max_len = len(l)
                l = []
                left += 1
                ptr = left

        if l:
            if len(l) > max_len:
                max_len = len(l)

        return max_len