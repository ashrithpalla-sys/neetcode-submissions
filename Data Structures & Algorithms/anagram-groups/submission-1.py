class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)

            if key not in anagram_dict:
                anagram_dict[key] = [word]
            else:
                anagram_dict[key].append(word)
        
        return list(anagram_dict.values())



