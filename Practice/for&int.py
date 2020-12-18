# for i in range(1,21):
#     print(i)
#
# list100 = [value for value in range(1,101)]
# print(list100)
#
# print(min(list100))
# print(max(list100))
# print(sum(list100))
# listjishu = [value for value in range(1, 21, 2)]
# print(listjishu)
#
# listb3zc = [value for value in range(3, 31, 3)]
# print(listb3zc)
# for i in listb3zc:
#     print(i)
listlf = []
for b in range(1, 11):
    c = b**3
    print(c)
    listlf.append(c)
print(listlf)

list3cf = [value**3 for value in range(1,11)]
for a in list3cf:
    print(a)