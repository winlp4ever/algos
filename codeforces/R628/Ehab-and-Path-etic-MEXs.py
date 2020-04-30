def run():
    n = int(input())
    edges = []
    graph = [0 for i in range(n)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append([u-1, v-1])
        graph[u-1] += 1
        graph[v-1] += 1
    for k in range(n):
        if graph[k] >= 3:
            h = 0
            l = graph[k]
            for e in edges:
                if e[0] == k or e[1] == k:
                    print(h)
                    h += 1
                else:
                    print(l)
                    l += 1
            return 
        
    for i in range(n-1):
        print(i)

run()