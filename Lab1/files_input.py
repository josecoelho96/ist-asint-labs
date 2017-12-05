f = open('data', 'r')

s1 = f.read()
print s1

v1 = f.readlines()
for s in v1:
    print s