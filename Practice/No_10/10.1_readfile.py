# with open('pi.digits.txt') as text_file:
#     pae = text_file.read()
#     print(pae)
#     print(pae.rstrip())

filename = 'pi.digits.txt'

with open(filename) as text_file:
    lines = text_file.readlines()

pi_string = []
for line in lines:
    pi_string.append(line)

print(pi_string)
print(len(pi_string))
