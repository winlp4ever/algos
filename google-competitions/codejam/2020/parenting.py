t = int(input())

def sol():
    n = int(input())
    actis = []
    for i in range(n):
        st, en = map(int, input().split())
        actis.append([st, en, i])
    actis.sort()

    a = ['N' for _ in range(n)]
    J = -1
    C = -1
    for st, en, i in actis:
        if st >= J:
            a[i] = 'J'
            J = en 
        elif st >= C:
            a[i] = 'C'
            C = en
        else:
            return 'IMPOSSIBLE'
    res = ''
    for c in a:
        res += c
    return res

for i in range(1, t+1):
    print('Case #{}: {}'.format(i, sol()))
        
        

