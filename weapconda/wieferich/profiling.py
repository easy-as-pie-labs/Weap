__author__ = 'easy as pie labs'

from timeit import default_timer as timer
import numpy as np
from wieferich import *
from utils import *


def block_thread_test(blocks, threads):
    """
    runs wieferich search with given block and thread dimensions
    :param blocks: blocks to use
    :param threads: thread to use per block
    :return: needed seconds for 10k numbers
    """
    runs = 100
    size = blocks * threads
    start_timer = timer()
    for i in range(runs):
        start = 6700000000000001 + (i * size)
        check = create_list(start, size)
        result = np.zeros(size, dtype=np.uint64)

        wieferich[blocks ,threads](check, result)

    times = timer() - start_timer

    return times / (size/10000) / runs


def block_thread_test_initializer():
    """
    test different block and thread combinations
    :return:
    """
    threads = [128, 256, 512, 1024]
    blocks = [(100, "0.1k"), (500, "0.5k"), (1000, "1k"), (5000, "5k"), (10000, "10k"), (50000, "50k"), (100000, "100k")]
    times = []

    plot_times = []
    plot_labels = []

    for i in threads:
        thread_times = []
        for j in blocks:
            time_in_s = block_thread_test(j[0], i)
            thread_times.append((j[0], i, round(time_in_s, 5)))
            plot_times.append(time_in_s*1000)
            plot_labels.append(j[1] + ", " + str(i))

            print ("Threads: %d, Blocks: %d, Time: %f" % (i, j[0], time_in_s))
        times.append(thread_times)

    #print (times)

    best_combination = [(1, 1, 1)]
    for x in times:
        for y in x:
            if y[2] < best_combination[0][2]:
                best_combination = [y]
            elif y[2] == best_combination[0][2]:
                best_combination.append(y)

    print (best_combination)
    profiling_bar_chart(plot_times, plot_labels)
    save_to_file(times, 'block_thread_test.txt')


def wieferich_vs_fermatwieferich_test():
    """
    runs wieferich search with given block and thread dimensions
    :param blocks: blocks to use
    :param threads: thread to use per block
    :return: needed seconds for 10k numbers
    """
    runs = 100
    blocks = 50000
    threads = 256
    size = blocks * threads
    start_timer = timer()
    for i in range(runs):
        start = 6700000000000001 + (i * size)
        check = create_list(start, size)
        result = np.zeros(size, dtype=np.uint64)

        wieferich[blocks ,threads](check, result)

    times1 = timer() - start_timer

    start_timer = timer()
    for i in range(runs):
        start = 6700000000000001 + (i * size)
        check = create_list(start, size)
        result = np.zeros(size, dtype=np.uint64)

        fermat_wieferich[blocks ,threads](check, result)

    times2 = timer() - start_timer

    return (times1 / (size/10000) / runs), (times2 / (size/10000) / runs)



if __name__ == '__main__':
    print wieferich_vs_fermatwieferich_test()
