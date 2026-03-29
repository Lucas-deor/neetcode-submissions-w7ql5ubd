class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false
        }

        const sMap = new Map()
        const tMap = new Map()

        for (let i = 0; i < s.length; i++) {
            sMap[s[i]] = (sMap[s[i]] || 0) + 1;
            tMap[t[i]] = (tMap[t[i]] || 0) + 1;
        }

        for (const key in sMap) {
            if (sMap[key] !== tMap[key]) {
                return false
            }
        }

        return true;
    }
}
