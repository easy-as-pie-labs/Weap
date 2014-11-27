from __future__ import print_function, division
import numpy as np
from timeit import default_timer as timer
from numbapro import cuda
from thread import start_new_thread


@cuda.jit('uint64(uint64, uint64, uint64)', inline=True, device=True)
def modexp(base, exponent, p):
    """
    iterative modular expoentiation
    :param base:
    :param exponent:
    :param p:
    :return:
    """
    result = 1
    base = base % p
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result*base) % p
        exponent = exponent >> 1
        base = (base*base) % p

    return result


@cuda.jit('void(uint64[:], uint64[:])', target='gpu')
def wieferich(check, result):
    """
    checks if a given number is a wieferich prime
    :param check: list of numbers to check
    :param result: list of wieferich numbers (or 0)
    :return:
    """
    #current index
    i = cuda.grid(1)
    ac = check[i]

    #modexp params
    m = 2
    e = ac-1
    n = ac**2

    if modexp(m, e, n) == 1:
        result[0] = ac



@cuda.jit('void(uint64[:], uint64[:])', target='gpu')
def fermat_wieferich(check, result):
    """
    checks if a given number is composite fermat
    :param check: list of numbers to check
    :param result: list of composite fermats numbers (or 0)
    :return:
    """
    #current index
    i = cuda.grid(1)
    ac = check[i]

    #params for fermat-check
    m = 2
    e = ac-1
    n = ac

    #if fermat run wieferich-check
    if modexp(m, e, n) == 1:
        n = ac**2
        if modexp(m, e, n) == 1:
            result[i] = ac


def main():

    RUNS = 100000
    time_deltas = []

    BLOCKS = 50000
    THREADSPERBLOCK = 256
    SIZE = BLOCKS * THREADSPERBLOCK

    wieferichs = []
    overall_timer_start = timer()
    for i in range(RUNS):
        start = 6700000000000001 + (i * SIZE)
        if i % 500 == 0:
            print (str(i) + "th Run, checking from " + str(start) + " to " + str(start+SIZE))
        check = create_list(start, SIZE)
        #result = np.zeros(SIZE, dtype=np.uint64)
        result = np.zeros(1, dtype=np.uint64)

        start_time = timer()

        wieferich[BLOCKS, THREADSPERBLOCK](check, result)

        needed_time = timer() - start_time
        time_deltas.append(needed_time)
        #print ("%f seconds" % needed_time)

        #start threaded result processing
        start_new_thread(proc_result,(result[0], start))
        #proc_result(result, i)
        #print(result)

    time_in_seconds = timer() - overall_timer_start
    import datetime
    execution_delta = str(datetime.timedelta(seconds=time_in_seconds))
    print("time: " + execution_delta + " for %d numbers" % ((SIZE*RUNS)))
    print (datetime.datetime.today())

    # save times to file
    f = open('time.txt', 'a')
    for item in time_deltas:
        print(str(item), file=f)
    f.close()

    import matplotlib.pyplot as plt

    plt.title("Execution per block")
    plt.xlabel("xth block (" + str(SIZE) + " numbers per block)")
    plt.ylabel("execution time in seconds")
    plt.plot(time_deltas)
    #plt.savefig("overnight.png")
    #plt.show()


def create_list(start, size):
    """
    creates a np list of odd numbers
    :param start: start of list
    :param size: size of list
    :return: list
    """
    if start % 2 != 1:
        start += 1
    list = np.arange(start, start+size*2, 2, dtype=np.uint64)

    return list

def proc_result(result, start):
    """
    process results -> needs to be threaded properly
    :param result: result to be processed
    :param name: thread count
    :return:
    """
    if result == 0:
        return

    print(result)

    f = open('wieferichs.txt', 'a')
    print(str(result) + " in range from " + str(start), file=f)
    f.close()


if __name__ == '__main__':
    main()
    #from profiling import test
    #test()