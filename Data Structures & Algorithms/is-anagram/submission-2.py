class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        hashmap = dict()

        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] = 1

        for i in t:
            if i in hashmap:
                hashmap[i]-=1
            else:
                hashmap[i] = 1

        for i in hashmap.values():
            if i != 0:
                return False
        return True
