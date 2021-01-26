# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!!!")


# filename = "alice.txt"
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f'{filename} is not exist!')


# title = "Alice in Wonderland"
# print(title.split())
# changdu = title.split()
#
# print(len(changdu))
# print(len(title))

while True:
    try:
        x = float(input("请输入第一个数字："))
    except NameError or ValueError:
        print("请输入一个《数字》哦")
        continue
    else:
        xx = int(x)
        break

while True:
    try:
        y =float(input("请输入第二个数字："))
    except NameError or ValueError:
        print("请输入一个《数字》哦")
        continue
    else:
        yy = int(y)
        break

z = xx + yy
print(z)


