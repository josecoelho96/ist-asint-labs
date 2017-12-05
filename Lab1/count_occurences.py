f = open('numbers', 'r')

lines = f.readlines()
dict = {}

for line in lines:
    value = line[:-1]

    if value not in dict:
        dict[value] = 1
    else:
        dict[value] = dict[value]+1

print dict