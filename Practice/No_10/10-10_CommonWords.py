b = 0
with open("The Little Pets of Arkkhan.txt") as book:
    for i in book:
        a = i.lower().count("the")
        b = b + a

print(b)