def sol():
    # input 
    n = int(input())
    patterns = []
    for _ in range(n):
        s = input()
        patterns.append('#' + s + '#')
    
    st = []
    for p in patterns:
        st.append(p.split('*'))
    fs, md, en = '#', '', '#'
    for u in st:
        if fs in u[0]:
            fs = u[0]
        elif u[0] not in fs:
            return '*'
        if en in u[-1]:
            en = u[-1]
        elif u[-1] not in en:
            return '*'
        
        for mor in u[1:-1]:
            md += mor + '*'
    return (fs + '*' + md + en)[1:-1].replace('*', '')
    


t = int(input())
for i in range(1, t+1):
    print('Case #{}: {}'.format(i, sol()))