class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()

        def loop(i):
            if i:
                if len(i) == 1:
                    return i[0][::-1]
                
                return i[0][::-1] + " " + loop(i[1:])


        return loop(s)