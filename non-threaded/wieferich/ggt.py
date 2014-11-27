__author__ = 'TPei'
from timeit import default_timer as timer

def extendedGcd(a, b):
    """
    is this better?
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a, 1, 0
    else:
        q, u, v = extendedGcd(b, a%b)
        q = a // b
        return q, v, u - q*v


def ggt(a, b):
    """
    groesster gemeinsamer Teiler
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a
    else:
        return ggt(b, a % b)


def profiling():
    """
    profiling ggt and extended ggt
    :return:
    """
    start = timer()
    for i in range(0, 1000):
        for j in range(0, 1000):
            ggt(i, j)
    ggt_time = timer() - start

    start = timer()
    for i in range(0, 1000):
        for j in range(0, 1000):
            extendedGcd(i, j)
    egcd_time = timer() - start

    return ggt_time, egcd_time

if __name__ == '__main__':
    print profiling()