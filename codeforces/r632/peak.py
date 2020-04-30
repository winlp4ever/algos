from collections import deque

t = int(input())

def sol():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    peaks = deque()
    for i in range(1, k-1):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            peaks.append(i)
    pM = len(peaks)
    l = 0
    for i in range(k, n):
        if peaks and peaks[0] == i-k+1:
            peaks.popleft()
        if a[i-1] > a[i-2] and a[i-1] > a[i]:
            peaks.append(i-1)
        if len(peaks) > pM:
            pM = len(peaks)
            l = i-k+1
    return pM+1, l+1

for i in range(t):
    u, v = sol()
    print(u, v)