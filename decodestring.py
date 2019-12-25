'''
Problem:

'''

class Solution:
    '''
    complexity: O(n^2) in time, O(n) in space
    '''
    def decodeString(self, s: str) -> str:
        digits = {str(i) for i in range(10)}
        s = '1[%s]'%s
        pos = []
        strs = []
        h = 0
        for i,c in enumerate(s):
            if c == '[':
                le = i-1
                while s[le] in digits:
                    le -= 1
                pos.append((le+1, i-le-1))
                h += 1
            elif c == ']':
                j, k = pos.pop()
                s_ = s[j+k+1:i]
                while strs and strs[-1][-1] > h:
                    l, r, sub, _ = strs.pop()
                    s_ = s_[:l-j-k-1] + sub + s_[r-j-k:]
                strs.append((j, i, s_ * int(s[j:j+k]), h))
                h -= 1
        return strs[-1][2]