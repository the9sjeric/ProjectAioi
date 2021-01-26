name = 'learning_python.txt'
with open(name) as one:
    youread = one.read()
    print(youread.replace("python","cat"))
# print(youread)
# print("aaaaaa")
#
# with open(name) as two:
#     try:
#         while True:
#             youreadline = two.readline()
#             if youreadline:
#                 print(youreadline)
#             else:
#                 break
#     finally:
#         print("bbbbbb")
#
# yrls = []
# with open(name) as three:
#     youreadlines = three.readlines()
#     for i in youreadlines:
#         yrls.append(str(i))
# print(yrls)



