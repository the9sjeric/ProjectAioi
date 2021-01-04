# sandwich_orders = ["aaa", "bbb", "ccc"]
# finish_sandwich = []
# while sandwich_orders:
#     xyz = sandwich_orders.pop()
#     print(f"I made {xyz}")
#     finish_sandwich.append(xyz)
# print(finish_sandwich)

# sandwich_orders = ["bbb", "aaa", "bbb", "ccc", "bbb"]
# print("bbb is sold out.")
# while "bbb" in sandwich_orders:
#     sandwich_orders.remove("bbb")
# print(sandwich_orders)

travel = {}
jieshu = True
while jieshu:
    name = input("\nwhat your name?")
    place = input("\nwhere you wangt to go?")
    travel[name] = place

    jieguo = input("\nend? (yes\\no)")
    if jieguo == "yes":
        jieshu = False
print(travel)