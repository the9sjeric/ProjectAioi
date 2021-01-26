import json

# number = input("请输入一个你喜欢的数字！")
#
# with open("numbers.json","w") as f:
#     json.dump(number, f)
#     print(f"我知道了，你最喜欢的数字是{number}！")

try:
    with open("numbers.json") as f:
        x = json.load(f)
#         print(x)
except json.decoder.JSONDecodeError or IndentationError:
    number = input("请输入一个你喜欢的数字：")
    with open("numbers.json", "w") as f:
        json.dump(number, f)
        print(f"你最喜欢的数字是{number},我已经记住了！")
else:
    with open("numbers.json") as b:
        y = json.load(b)
        print(f"我知道的，你最喜欢的是{y}")