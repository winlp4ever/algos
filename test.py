a = {1, 5, 7}
it = iter(a) 
u = -1
while u:
    u = next(it, None)
    print(u)