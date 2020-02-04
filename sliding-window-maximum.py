from collections import deque
def solution(nums, k):
    if not nums:
        return []
    n = len(nums)
    memo = deque()
    sol = []
    for i,u in enumerate(nums[:k]):
        while memo:
            if memo[-1][0] <= nums[i]:
                memo.pop()
            else:
                break
        memo.append((u, i))
    sol.append(memo[0][0])
    for i in range(k, n):
        if memo[0][1] == i-k:
            memo.popleft()
        while memo:
            if memo[-1][0] <= nums[i]:
                memo.pop()
            else:
                break
        memo.append((nums[i], i))
        sol.append(memo[0][0])
    return sol

if __name__ == '__main__':
    a = [9,10,9,-7,-4,-8,2,-6]
    k = 5
    print(solution(a, k))