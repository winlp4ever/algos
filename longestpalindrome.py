# level: easy
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        ld = dict()
        for c in s:
            if c not in ld:
                ld[c] = 0
            ld[c] += 1
        pip = 0
        l = 0
        for _, v in ld.items():
            if v % 2 == 1:
                pip = 1
            l += 2 * (v//2)
        return l + pip