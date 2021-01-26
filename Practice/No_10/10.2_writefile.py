# filename = "programming.txt"
#
# with open(filename,'a') as file_object:
#     file_object.write("\nI love programming.")

# name = input("请输入你的名字:")
#
# with open('guest.txt', 'a') as guestlist:
#     guestlist.write('\n' + name)

while True:
    guestname = input("请输入你的名字")
    with open('guest_list.txt', 'a') as guestlist:
        guestlist.write(guestname + '\n')