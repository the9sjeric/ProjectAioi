class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def readnum(self):
        print("lai dian ren shu " + str(self.number_served) )

    def describe_restaurant(self):
        print(self.name + " 是一家 " + self.type + " 类型的餐厅." )

    def open_restaurant(self):
        print(self.name + " is openning.")

    def set_number_served(self,initnum):
        self.number_served = initnum

    def increment_number_served(self,incrementnum):
        self.number_served += incrementnum

my = Restaurant("aaa","bbb")
my.readnum()
my.set_number_served(666)
my.readnum()
my.increment_number_served(222)
my.readnum()
my.describe_restaurant()




