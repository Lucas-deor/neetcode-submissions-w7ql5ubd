class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    scoreOfString(s) {
        let ans = 0

        for (let i = 0; i < s.length; i++) {
            if (i + 1 < s.length) {
                ans = ans + Math.abs(s.charCodeAt(i) - s.charCodeAt(i + 1))
            }
        }
        return ans
    }
}
