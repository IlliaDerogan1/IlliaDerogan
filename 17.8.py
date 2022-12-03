from collections import Counter

def mydecorator(f):
    def check(*args,**kw):
        for l in args:
            if not l == str(l):
                raise TypeError ('\"{0}\" цей елемент не є рядком.'.format(l))
        for l in kw:
            if not l == int(l):
                raise TypeError ('\"{0}\" цей елемент не є рядком.'.format(l))
        print(f(*args))
    return check


@mydecorator
def listcreator(*args):
    list = []
    list1 = []
    for i in args:
        if i not in list: list.append(i)
        j = i.split()
        for k in j:
            list1.append(k)
    print(max(set(list1), key=lambda x: list1.count(x)))
    return list

def main():
    listcreator('yabluko yabluko аппва','sluva','grusha','persuk','granat','ananas','kiwi','abrucos','wushnya','puvo')


if __name__ == '__main__':
    main()
