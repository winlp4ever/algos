t = int(input())

def sol():
    s = input()
    digits = []
    for c in s:
        digits.append(int(c))
    k = 0
    nsting = ''
    for d in digits:
        diff = d - k
        if diff > 0:
            nsting += '(' * diff + str(d)
        elif diff < 0:
            nsting += ')' * (-diff) + str(d)
        else: 
            nsting += str(d) 
        k = d 
    nsting += ')' * digits[-1] 
    return nsting 

for i in range(1, t+1):
    nsting = sol()
    print('Case #{}: {}'.format(i, nsting))   