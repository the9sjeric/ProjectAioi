try:
    with open("catss.txt") as f:
        for i in f:
            print(i.rstrip())
except FileNotFoundError:
    print("沉默")

print("--------------------")

with open("dogs.txt") as f:
    for i in f:
        print(i.rstrip())
