'''
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1
'''

import sys

def search(a, val):
    # binary search: given an increasing array and a value, return index of largest ele <= value
    if not a or a[0] > val:
        return -1
    if a[-1] <= val:
        return len(a)-1
    def binSearch(lo, hi):
        if lo+1 >= hi:
            return lo
        mi = (lo+hi) // 2
        if a[mi] <= val:
            return binSearch(mi, hi)
        return binSearch(lo, mi) 
    return binSearch(0, len(a)-1)

class Solution:
    '''
    Complexity: O(n) time and O(1) space, if do rigorously
    Question: why using sort but end up O(n) time? because the sort-needed array is almost sorted
    '''
    def nextGreaterElement(self, n: int) -> int:
        nums = list(map(lambda u: int(u), list(str(n))))
        l = len(nums)
        for i in range(l-2, -1, -1):
            if nums[i] < nums[i+1]:
                a = nums[i]
                nums[i:] = sorted(nums[i:])
                arr = nums[i:]
                idx = search(arr, a)+1
                res = int(''.join(map(lambda u: str(u), [*nums[:i], arr[idx], *arr[:idx], *arr[idx+1:]])))
                return res if (res > n and res <= (2**31-1)) else -1
        return -1


def test_search():
    a = int(sys.argv[1])
    nums = list(map(lambda u: int(u), list(str(a))))
    print(nums)
    b = int(sys.argv[2])
    print(b)
    print(search(nums, b))


def test_sol():
    n = int(sys.argv[1])
    print(n)
    sol = Solution()
    print(sol.nextGreaterElement(n))

if __name__ == '__main__':
    #test_search()
    test_sol()
    