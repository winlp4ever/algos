'''
Problem: link: https://leetcode.com/problems/longest-repeating-character-replacement/
'''

def foo(l, k: int) -> int:
    # longest contiguous subseq whose sum infe or equal to k        
    i = 0
    j = 0
    lg = 0
    sm = 0
    n = len(l)
    while j < n:
        sm += l[j]
        while sm > k:
            sm -= l[i]
            i += 1
        if j-i+1 > lg:
            lg = j-i+1
        j += 1 
    return lg
    
    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memo = dict()
        last_pos = dict()
        for i, c in enumerate(s):
            if c not in memo:
                memo[c] = []
                last_pos[c] = i
            else:
                memo[c].append(i - last_pos[c] - 1)
                last_pos[c] = i
        longest = 0
        for c in memo:
            ln = foo(memo[c], k)
            if longest < ln:
                longest = ln
        return min(longest + 1 + k, len(s))