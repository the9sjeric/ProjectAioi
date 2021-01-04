# def get_name(first, last):
#     full = first + ' ' + last
#     return full.title()
#
# myname = get_name("shen", "jian")
# print(myname)

# def build_person(firstname, lastname):
#     person = {"first":firstname, "last":lastname}
#     return person
#
#
# ren = build_person("shen", "jian")
# print(ren)

# def cities(city,country):
#     cityname = city + ',' + country
#     return cityname
#
#
# print(cities("hangzhou", "China"))
# print(cities("tokyo", "Japan"))
# print(cities("newyork", "Ammerican"))

def make_album(names, songs, shuliang=''):
    zhuanji = {"singer":names, "zjm":songs}
    if shuliang:
        zhuanji['shuliang'] = shuliang
    return zhuanji
# print(make_album("liudehua", "bingyu",'25'))
# print(make_album("smna", "yishengyouni"))
# print(make_album("zhoujielun", "ninja"))
while True:
    x = input("请输入歌手名")
    if x == "q":
        break
    y = input("请输入专辑名")
    if y == "q":
        break
    z = input("请输入专辑名")
    if z == "q":
        break
    print(make_album(x, y, z))
