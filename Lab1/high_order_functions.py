def double(x):
    return 2*x

lst = range(10)

print lst

new_lst = map(double, lst)

print new_lst


def even(x):
    return x % 2 == 0

new_lst_2 = filter(even, lst)
print new_lst_2

def plus(x, y):
    return (x+y)

new_lst_3 = reduce(plus, lst)
print new_lst_3