def mydecorator(f):
    def check(*args):
        for l in args:
            if not type(l) == type(args):
                raise TypeError ('\"{0}\" цей елемент не є рядком.'.format(l))
        print('\n Вигляд  списку такий :')
        print(f(*args))
    return check


@mydecorator
def listcreator(*args):
    list = []
    sum = 0
    for i in args:
        if i not in list: list.append(i)
    for j in len(list):
        sum += j
    average = sum/len(list)
    return list

def main():
    listcreator('12','56.09','-2','0','6547','84.12211243','1','32','812','4')
