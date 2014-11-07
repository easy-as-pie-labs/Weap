from threading import Thread
def binary(e):
    return bin(e)[2:]

def modexp(m, e, n):
    if e == 0:
        return 1
    if e % 2 == 1:
        return modexp(m, e-1, n) * m % n
    else:
        return modexp(m, e//2, n) ** 2 % n

def isWieferich(n):
    return modexp(2, n-1, n**2) == 1

class MyThread(Thread):
    def __init__(self, rangeStart, rangeEnd):
        Thread.__init__(self)
        self.rangeStart = rangeStart
        self.rangeEnd = rangeEnd

    def run(self):
        self.searchWieferich()

    def searchWieferich(self):
        i = self.rangeStart
        if i % 2 == 0:  #ensures that start is an odd number
            i += 1
        while i <= self.rangeEnd:
            if(isWieferich(i)):
                print self.name + " might have found a wieferich: " + str(i)
            if(i%100000 == 1):
                print self.name + " currently at: " + str(i)
            i += 2

if __name__ == '__main__':
    firstThread = MyThread(10**17, 10**18)
    firstThread.setName('Thread 1')
    secondThread = MyThread(10**18,  10**19)
    secondThread.setName('Thread 2')
    thirdThread = MyThread(10**19, 10**20)
    thirdThread.setName('Thread 3')
    fourthThread = MyThread(10**20, 10**21)
    fourthThread.setName('Thread 4')

    firstThread.start()
    secondThread.start()
    '''
    thirdThread.start()
    fourthThread.start()
    '''