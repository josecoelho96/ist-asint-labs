f = open('numbers', 'r')

lines = f.readlines()
arr = []

for line in lines:
    arr.append(line[:-1])

print arr