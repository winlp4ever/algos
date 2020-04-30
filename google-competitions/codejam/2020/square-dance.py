class Dancer:
    def __init__(self, i, j, val):
        self.val = val
        self.i = i 
        self.j = j 
        self.w = None 
        self.e = None 
        self.n = None 
        self.s = None

    def isTer(self):
        c = 0
        sm = 0
        if self.w: 
            sm += self.w.val 
            c += 1
        if self.e:
            sm += self.e.val 
            c += 1
        if self.s:
            sm += self.s.val
            c += 1
        if self.n:
            sm += self.n.val 
            c += 1
        if c > 0 and self.val < sm / c:
            return True 
        return False
def sol():
    # input
    r,c = map(int, input().split())
    arr = [[None for _ in range(c)] for _ in range(r)]
    for i in range(r):
        line = input().split()
        for j in range(c):
            arr[i][j] = Dancer(i, j, int(line[j]))
    todel = set()
    A = 0
    for i in range(r):
        for j in range(c):
            if i > 0:
                arr[i][j].n = arr[i-1][j]
            if j > 0:
                arr[i][j].w = arr[i][j-1]
            if i < r-1:
                arr[i][j].s = arr[i+1][j]
            if j < c-1:
                arr[i][j].e = arr[i][j+1]
            if arr[i][j].isTer():
                todel.add((i, j))
            A += arr[i][j].val
    #print(A)
    S = A
    rnd = 0
    while len(todel) > 0:
        todel_ = set()
        for i, j in todel:
            u = arr[i][j]
            A -= u.val
            if u.n:
                u.n.s = u.s 
            if u.s:
                u.s.n = u.n  
            if u.w:
                u.w.e = u.e
            if u.e:
                u.e.w = u.w
        for i, j in todel:
            u = arr[i][j]
            if u.n and u.n.isTer() and (u.n.i, u.n.j) not in todel:
                todel_.add((u.n.i, u.n.j))
            if u.s and u.s.isTer() and (u.s.i, u.s.j) not in todel:
                todel_.add((u.s.i, u.s.j))
            if u.w and u.w.isTer() and (u.w.i, u.w.j) not in todel:
                todel_.add((u.w.i, u.w.j))
            if u.e and u.e.isTer() and (u.e.i, u.e.j) not in todel:
                todel_.add((u.e.i, u.e.j))
        rnd += 1
        todel = todel_
        S += A
    return S

t = int(input())
for i in range(1, t+1):
    print('Case #{}: {}'.format(i, sol()))
            
