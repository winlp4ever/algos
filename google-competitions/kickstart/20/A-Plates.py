import heapq

T = int(input())

def case():
    # input
    n, k, p = list(map(int, input().split()))
    stacks = []
    for i in range(n):
        lst = list(map(int, input().split()))
        Q = [0]
        for e in lst:
            Q.append(Q[-1] + e)
        stacks.append(Q)

    # algorithm
    # dynamic programming
    dp = [[0 for _ in range(p+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for q in range(p+1):
            for h in range(min(q, k)+1):
                dp[i][q] = max(dp[i][q], dp[i-1][q-h] + stacks[i-1][h])
    return dp[-1][-1]

for c in range(T):
    print('#{}: {}'.format(c+1, case()))

