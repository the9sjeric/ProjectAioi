magics = ["aaa", "bbb", "ccc"]
def show_magicians(xxx):
    for i in xxx:
        print(i)
show_magicians(magics)

zzz = []
def make_great(yyy):
    z = len(yyy)
    for i in range(0, z):
        yyy[i] = 'The Great ' + yyy[i]
        zzz.append(yyy[i])


make_great(magics[:])
show_magicians(magics)
print(magics)
print(zzz)

