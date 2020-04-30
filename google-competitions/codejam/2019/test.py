u = {0: [1, 2], 1: [3]}
v = min(range(2), key=lambda a: len(u[a]))
print(v)