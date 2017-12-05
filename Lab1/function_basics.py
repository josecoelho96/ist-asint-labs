def max(x, y):
    if x < y:
        return x
    else:
        return y

def div(x, y):
    return x/y, x%y


print max(5, 4)
print div(4, 2)
print div(5, 3)