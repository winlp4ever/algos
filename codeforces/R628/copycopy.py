T = int(input())

for _ in range(T):
    n = int(input())
    print(len(set(map(int, input().split()))))