class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_value = 1000
        L = 0

        for R in range(k - 1, len(blocks)):
            aux_str = blocks[L:R+1]
            amount_w = aux_str.count("W")
            min_value = min(min_value, amount_w)
            L += 1
            
        return min_value