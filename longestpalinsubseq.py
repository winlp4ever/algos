from typing import List

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        dp = dict()
        def rec(s_):
            if len(s_) < 2:
                return len(s_)
            if s_ in dp:
                return dp[s_]
            res = max(rec(s_[1:-1]) + 2*(s_[0] == s_[-1]), rec(s_[1:]), rec(s_[:-1]))
            dp[s_] = res 
            return res 
        return rec(s)

if __name__ == '__main__':
    s = 'aaaaaaaaaaaaaaaaaaaa'
    sol = Solution()
    print(sol.longestPalindromeSubseq(s))