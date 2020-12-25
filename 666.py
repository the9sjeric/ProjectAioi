g = [2, 1, 2, 3]
s = [2, 1, 1, 2]
g = sorted(g)
print(g)
s = sorted(s)
print(s)
ss = len(s) - 1
j = 0
for i in range(0, ss):
    if s[i] >= g[j]:
        j = j + 1
print(j)