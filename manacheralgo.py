'''
An implementation of Manachers' algorithm for 
finding longest palindrome substring

Complexity: O(n) time and space
Why O(n) time:
* A simple analysis of the algorithm will mistell us that the complexity is O(n^2)
however, it is in fact O(n), because the loop while in the algorithm run only 1 iter
if P[i] = P[i_]
'''
import sys

def manachers(s: str) -> int:
    s = _transi(s)
    if not s:
        return 0

    n = len(s)    
    c = r = 0

    maxlen = 0
    P = [0 for _ in s] # array to store expanded length of palindrome centered at i

    for i in range(n):
        # find mirror index
        i_ = 2*c - i
        if i < r:
            P[i] = min(r-i, P[i_] if i_ >= 0 else float('inf'))
        # expand
        a = i-P[i]
        b = i+P[i]
        while a > 0 and b < n-1:
            a -= 1
            b += 1
            if s[a] == s[b]:
                P[i] += 1
            else:
                break
        if i+P[i] > r:
            c = i
            r = i+P[i]
        if P[i] > maxlen:
            maxlen = P[i]
    return maxlen


def _transi(s: str) -> str:
    '''
    Transform any string a1a2...an to #a1#a2#...#an# to ensure 
    every palindrome substr has odd length
    '''
    s_ = '#'
    for c in s:
        s_ += c + '#'
    return s_


if __name__ == '__main__':
    s = sys.argv[1]
    print(manachers(s))