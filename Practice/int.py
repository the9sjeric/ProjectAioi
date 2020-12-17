for value in range(1, 5):
    print(value)

shuzi = list(range(2, 7, 2))
print(shuzi)

pingfang = []
for i in range(1, 11):
    # aaa = i ** 2
    pingfang.append(i**2)
print(pingfang)

print(min(pingfang))
print(max(pingfang))
print(sum(pingfang))

xin = [b**2 for b in range(1,6)]
print(xin)