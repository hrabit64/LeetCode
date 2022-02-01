from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_hash = defaultdict(int)
        
        for i in s1:
            
            s1_hash[i] += 1
        
        for i in range(len(s2)):
            s2_hash = defaultdict(int)
            for x in s2[i:i+len(s1)]:
                s2_hash[x] += 1
            
            if s1_hash == s2_hash:
                return True
        
        return False