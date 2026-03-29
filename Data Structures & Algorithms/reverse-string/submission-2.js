class Solution {
    /**
     * @param {character[]} s
     * @return {void} Do not return anything, modify s in-place instead.
     */
    reverseString(s) {
        let l = 0;
        let r = s.length - 1;

        while (l < r) {
            let aux_sl = s[l]
            let aux_sr = s[r]

            s[l] = aux_sr
            s[r] = aux_sl

            l++
            r--
        }
    }
}
