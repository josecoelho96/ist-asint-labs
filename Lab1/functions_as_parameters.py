def foo(f, a):
    return f(a)

def bar(a):
    return a*a

print foo(bar, 3)