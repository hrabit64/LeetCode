    class Solution:

        def lengthOfLongestSubstring(self, s):
            start = maxLength = 0
            usedChar = {}

            for i in range(len(s)):
                if s[i] in usedChar and start <= usedChar[s[i]]:
                    start = usedChar[s[i]] + 1
                else:
                    maxLength = max(maxLength, i - start + 1)

                usedChar[s[i]] = i

            return maxLength
        
갯수 카운트 할 때는 해쉬맵 활용하여 속도 높이기
