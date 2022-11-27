class NonEqual(Exception):

    def __init__(self):
        super()

    def __str__(self):
        return 

def equalsizes(fun):
    def _equalsizes(*args, **kwargs):
        if len(args) != len(kwargs):
            raise NonEqual
        res = fun(*args, **kwargs)
        return res

    return _equalsizes

@equalsizes
def f1(*args, **kwargs):
    p = 1
    for x, y in zip(args, kwargs.values()):
        if y == 0:
            continue
        p *= (x + (1 / y))

    return p

if __name__ == '__main__':

    a1 = f1(1, 2, 3, y1=1, y2=2, y3=3)
    print("a=", a1)
    try:
        a1 = f1(1, 2, 3, y1=1, y2=2)
        print("a=", a1)
    except NonEqual as b:
        print("Caught exception: ", b)
