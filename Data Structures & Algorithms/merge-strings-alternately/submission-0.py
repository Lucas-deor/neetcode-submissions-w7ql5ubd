class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        aux_list = []

        def mergeStrings(s_word, b_word):
            i = 0
            while i < len(s_word):
                aux_list.append(word1[i])
                aux_list.append(word2[i])

                if i == len(s_word) - 1:
                    aux_string = "".join(aux_list)
                    return aux_string + b_word[i + 1:]

                i += 1

        if len(word1) >= len(word2):
            # usar word1
            return mergeStrings(word2, word1)
        else:
            # usar word1
            return mergeStrings(word1, word2)