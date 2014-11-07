from threading import Thread
from MathFunctions import *

class MyThread(Thread):
    def __init__(self, rangeStart, rangeEnd):
        Thread.__init__(self)
        self.rangeStart = rangeStart
        self.rangeEnd = rangeEnd

    def run(self):
        self.search_wieferich()

    def search_wieferich(self):
        i = self.rangeStart
        if i % 2 == 0:  #ensures that start is an odd number
            i += 1
        while i <= self.rangeEnd:
            if(MathFunctions.is_wieferich(i)):
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