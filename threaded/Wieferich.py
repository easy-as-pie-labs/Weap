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
        for i in range(self.rangeStart, self.rangeEnd):
            if(isWieferich(i)):
                print "might be wieferich: " + str(i)
            if(i%100000 == 1):
                print i
            i+=2

if __name__ == '__main__':
    firstThread = MyThread(10**17, 10**18)
    secondThread = MyThread(10**18, 10**19)
    thirdThread = MyThread(10**19, 10**20)
    fourthThread = MyThread(10**20, 10**21)

    firstThread.start()
    secondThread.start()
    thirdThread.start()
    fourthThread.start()


