# players = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
# print(players[:])

# myfood = ['aaa','bbb','ccc']
# herfood = myfood[:]
# print(herfood)
#
# myfood.append('yyy')
# herfood.append('xxx')
# print(myfood)
# print(herfood)

from pizza import make_pizza as mp
mp(32,"fanqie","niurou")


players = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']
print(f'The first three items in the list are {players[0:3]}')
print(f'The items from the middle of the list are {players[1:4]}')
print(f'The last three items of the list are {players[-3:]}')