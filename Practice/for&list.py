pizza = ['zhixin', 'haixian', 'niuyou']

for pisa in pizza:
    print(f'我喜欢吃{pisa.title()}披萨。')

print(f'{pizza[0]}披萨很软')
print(f'{pizza[1]}披萨很鲜')
print(f'{pizza[2]}披萨肉很多')
print(f'我太爱吃披萨了。我老婆最爱之{pizza[0]}')

friend_pizza = pizza[:]
pizza.append('zhurou')
friend_pizza.append('niuwa')
print(pizza)
print(friend_pizza)

# animal = ['dog', 'cat', 'mouse']
#
# for pet in animal:
#     a = animal[0]
#     b = animal[1]
#     c = animal[2]
#     if pet == a:
#         print(f'{pet.title()}听话，不过比较吵。')
#     else:
#         pass
#     if pet == b:
#         print(f'{pet.title()}非常安静，喜欢独立')
#     else:
#         pass
#     if pet == c:
#         print(f'{pet.title()}吃得少，不过寿命短')
# print('只要你喜欢，他们都是好宠物！')
