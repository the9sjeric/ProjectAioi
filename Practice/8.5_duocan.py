# def sandwich(toppings):
#     print('\n')
#     for topping in toppings:
#         print(f'- {topping}')
#
# kwj = ["jidan"]
# sll = ["jidan", "qingcai"]
# zm = ["mianbao", "xihongshi", "jiang"]
#
# sandwich(kwj)
# sandwich(sll)
# sandwich(zm)

# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['firstname'] = first
#     profile['lastname'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# print(build_profile('shen', 'jian', age=32, lenght=180, weight='70kg'))

def car_info(maker,model,**baseinfo):
    car = {}
    car['changjia'] = maker
    car['xinghao'] = model
    for key,value in baseinfo.items():
        car[key] = value
    return car


print(car_info('toyota', 'Rav4', age=2, colour='white'))