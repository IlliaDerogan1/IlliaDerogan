def mydecorator(f):
    def check(*args):
        for l in args:
            if not l == str(l):
                raise TypeError ('\"{0}\" цей елемент не є рядком.'.format(l))
        print('\n Вигляд  списку такий :')
        print(f(*args))
    return check


@mydecorator
def listcreator(*args):
    list = []
    for i in args:
        if i not in list: list.append(i)
    return list

def main():
    listcreator('yabluko','sluva','grusha','persuk','granat','ananas','kiwi','abrucos','wushnya','puvo')


