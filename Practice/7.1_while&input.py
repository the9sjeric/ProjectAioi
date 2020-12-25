# aaa = "Welcom to my python.\nPlease input your name:"
# name = input(aaa)
# print(f"Hello {name}")
# print(type(name))

#
# car = input("你需要租什么车？")
# print(f'OK,我知道你要{car}.')

# renshu = input("请问你们一共几个人就餐？")
# renshu = int(renshu)
# if renshu > 8:
#     print("没有大桌了，需要等待5小时。")
# else:
#     print("请进。")

shuzi = input("请输入一个数字。")
shuzi = int(shuzi)
jieguo = shuzi % 10
if jieguo == 0:
    print("10的整数")
else:
    print("shabi")