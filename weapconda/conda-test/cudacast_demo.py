import numpy as np
from timeit import default_timer as timer
from numbapro import vectorize

@vectorize(["uint64(uint64, uint64)"], target='gpu')
def vector_add(a, b):
    return a+b


def main():
    N = 1000000000

    A = np.ones(N, dtype=np.uint64)
    B = np.ones(N, dtype=np.uint64)
    C = np.zeros(N, dtype=np.uint64)

    start = timer()
    C = vector_add(A, B)
    needed_time = timer() - start

    print ("C[:5] = " + str(C[:5]))
    print ("C[-5:] = " + str(C[-5:]))

    print ("took massive %f seconds" % needed_time)

if __name__ == '__main__':
    main()