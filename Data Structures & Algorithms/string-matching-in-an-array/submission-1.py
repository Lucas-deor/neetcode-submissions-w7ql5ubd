class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and len(words[i]) < len(words[j]) and words[i] not in res:
                    res.append(words[i])
        
        return res





