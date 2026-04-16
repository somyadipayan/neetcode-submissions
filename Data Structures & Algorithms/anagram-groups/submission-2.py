class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            count_list = [0] * 26 # 26 0s for 26 alphabets
            for char in word:
                count_list[ord(char)-ord('a')] += 1
            output[tuple(count_list)].append(word)
        return list(output.values())

