from threading import Thread
from MathFunctions import *


class WieferichThread(Thread):
    def __init__(self, range_start, range_end):
        Thread.__init__(self)
        self.range_start = range_start
        self.range_end = range_end

    def run(self):
        self.search_wieferich()

    def search_wieferich(self):
        """
        search for wieferich
        """
        i = self.range_start
        if i % 2 == 0:  # ensures that start is an odd number
            i += 1
        while i <= self.range_end:
            if MathFunctions.is_wieferich(i):
                print self.name + " might have found a wieferich: " + str(i)
            i += 2

        print "Thread no. " + self.name + " finished"

if __name__ == '__main__':
    start = 6.7*10**15
    no_of_threads = 4
    block = 12800000 / no_of_threads

    for i in range(0, no_of_threads + 1):
        WieferichThread(start, start + block).start()
        start += block + 1