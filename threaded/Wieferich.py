from threading import Thread
def binary(e):
    return bin(e)[2:]

def modexp(m, e, n):
    s=1
    for b in binary(e):
        s=s*s % n
        if b=="1":
            s=s*m % n
    return s

'''
def isCompositeFermat(n):
    return modexp(2, n-1, n) != 1
'''

def isWieferich(n):
    return modexp(2, n-1, n**2) == 1

class MyThread(Thread):
    def __init__(self, rangeStart):
        Thread.__init__(self)
        self.rangeStart = rangeStart

    def run(self):
        self.searchWieferich()

    def searchWieferich(self):
        i = self.rangeStart + 1
        run = True
        while(run == True):
            if(isWieferich(i)):
                run = False
                print i
            if(i%100000 == 1):
                print i
            i+=2

myThreadOb1 = MyThread(10**17)
myThreadOb1.setName('Thread 1')

myThreadOb2 = MyThread(10**18)
myThreadOb2.setName('Thread 2')

myThreadOb3 = MyThread(10**17)
myThreadOb3.setName('Thread 3')

myThreadOb4 = MyThread(10**18)
myThreadOb4.setName('Thread 4')

myThreadOb1.start()
myThreadOb2.start()
myThreadOb3.start()
myThreadOb4.start()


