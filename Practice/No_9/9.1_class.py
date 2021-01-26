class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(self.name + " 是一家 " + self.type + " 类型的餐厅." )

    def open_restaurant(self):
        print(self.name + " is openning.")

myfandian = Restaurant("coffee","meido")
print(myfandian.name + myfandian.type)

zlyfd = Restaurant("huangmengji","liaolibao")
smufd = Restaurant("rourou","dandan")
myfandian.describe_restaurant()
zlyfd.describe_restaurant()
smufd.describe_restaurant()


