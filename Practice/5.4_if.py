# list = ['aaa','bbb','ccc','ddd','eee']
# want = ['aaa','xxx']
#
# for i in want:
#     if i in list:
#         print(f"add {i}")
#     else:
#         print(f"we dont have {i}")

# user = ['aaa','bbb','ccc','ddd','eee','admin']
# for i in user:
#     if i == 'admin':
#         print("welcome my root")
#     else:
#         print(f'hello {i}')

# list = []
# if list:
#     list.clear()
# else:
#     print("we need users")
# print(list)

# current_users = ['aaa','Bbb','ccc','ddd','eee']
# xx = [s.lower() for s in current_users]
# print(xx)
# new_users = ['Aaa','Bbb','fff','ggg','hhh']
# for i in new_users:
#     if i.lower() in xx:
#         print(f"{i} is exist.")
#     else:
#         print(f"{i} is able to use.")

shuzi = [1,2,3,4,5,6,7,8,9]
for i in shuzi:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")

