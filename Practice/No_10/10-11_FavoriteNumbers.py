import json

number = input("请输入一个你喜欢的数字！")

with open("numbers.json","w") as f:
    json.dump(number, f)
    print(f"我知道了，你最喜欢的数字是{number}！")

with open("numbers.json") as f:
    x = json.load(f)

print(x)