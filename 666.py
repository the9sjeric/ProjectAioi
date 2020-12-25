g = [0, 2, 2, 3]
s = [0, 1, 2, 2]
s = sorted(s)
g = sorted(g)
ss = len(s) - 1
j = 0
for i in range(0, ss):
    if s[i] >= g[j]:
        j = j + 1
print(j)