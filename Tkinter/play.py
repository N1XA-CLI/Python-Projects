def add(*args):
    a = 0
    for n in args:
        a += n

    return a

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *+ kwargs["multiply"]
    print(n)

print(add(1, 2, 5, 6, 7, 8, 9, 10))
calculate(2, add=3, multiply=5)
