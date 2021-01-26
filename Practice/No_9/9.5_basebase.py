from random import randint


class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = randint(1, Die().sides)
        print(x)


print(str(Die().sides))

print(str(Die().roll_die()))