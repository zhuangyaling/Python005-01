from log_test import Logger
l = Logger()
def sum(a):
    for i in range(10):
        a += i
        l.debug('message %d'%i)
    print(a)
sum(5)
