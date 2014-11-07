from __future__ import print_function
from MathFunctions import *
import os

'''
TODO:
put this in a class or whatever as a wrapper
put find wieferich etc somewhere else -> this should only be crud operartions...
'''

__author__ = 'goggelz / thomas'

prime = 1
wieferich = 1

'''
file name constants
'''
PRIMES_FILE = 'primes.txt'
WIEFERICHS_FILE = 'wieferichs.txt'
PRIME_COUNTER_FILE = 'counterPrime.txt'
WIEFERICHS_COUNTER_FILE = 'counterWieferichs.txt'


def write_to_file(filename, value, write_mode='a'):
    """
    abstract write to file function
    :param filename: file to save to
    :param value: value to save to file
    :param write_mode: mode to write in (default is a for append)
    :return:
    """
    f = open(filename, write_mode)
    print(value, file=f)
    f.close()


def write_prime(prime_to_save):
    """
    write prime to file
    :param prime_to_save:
    :return:
    """
    write_to_file(PRIMES_FILE, prime_to_save)


def write_wieferich(wieferich_to_save):
    """
    write wieferich to file
    :param wieferich_to_save:
    :return:
    """
    write_to_file(WIEFERICHS_FILE, wieferich_to_save)


def set_prime_counter(prime_count):
    """
    write prime count to file
    :param prime_count:
    :return:
    """
    write_to_file(PRIME_COUNTER_FILE, prime_count)


def set_wieferich_counter(wieferich_count):
    """
    write wieferich count to file
    :param wieferich_count:
    :return:
    """
    write_to_file(WIEFERICHS_COUNTER_FILE, wieferich_count)


def find_wieferichs():
    """
    endlessly find wieferich
    logging every 100000th number
    for progress monitoring
    :return:
    """
    global wieferich
    while True:
        wieferich += 2
        if MathFunctions.is_wieferich(wieferich):
            print (wieferich)
            write_wieferich(wieferich)
        if wieferich % 100000 == 1:
            print ("control: " + str(wieferich))
            set_wieferich_counter(wieferich)


def create_primes():
    """
    endlessly generate primes
    :return:
    """
    global prime
    while True:
        for x in range(2, prime, 1):
            if prime % x == 0:
                break
            if prime-1 == x:
                write_prime(prime)
        if prime % 10000 == 1:
            set_prime_counter(prime)
        prime += 2


def read_last_prime():
    """
    reads last prime from file
    :return:
    """
    global prime
    if not os.path.isfile(PRIMES_FILE):
        open(PRIMES_FILE, "a").close()

    f = open(PRIMES_FILE, "r")

    last = f.readlines()
    f.close()
    if last:
        prime = long(last[-1])+2
    return prime


def read_last_wieferich():
    """
    reads last wieferich from file
    :return:
    """
    global wieferich
    if not os.path.isfile(WIEFERICHS_FILE):
        open(WIEFERICHS_FILE, "a").close()

    f = open(WIEFERICHS_FILE, "r")

    last = f.readlines()
    f.close()
    if last:
        wieferich = long(last[-1])+2
    return wieferich


def get_prime_count():
    """
    gets prime count from file
    :return:
    """
    global prime
    if not os.path.isfile(PRIME_COUNTER_FILE):
        open(PRIME_COUNTER_FILE, "a").close()
    f = open(PRIME_COUNTER_FILE, "r")

    last = f.readlines()
    f.close()
    if last:
        prime = long(last[-1])+2
    return prime


def get_wieferich_count():
    """
    gets wieferich count from file
    :return:
    """
    global wieferich
    if not os.path.isfile(WIEFERICHS_COUNTER_FILE):
        open(WIEFERICHS_COUNTER_FILE, "a").close()
    f = open(WIEFERICHS_COUNTER_FILE, "r")

    last = f.readlines()
    f.close()
    if last:
        wieferich = long(last[-1])+2
    return wieferich


def init_wieferich():
    """
    initialize wieferich search program
    :return:
    """
    global wieferich
    if get_wieferich_count() > read_last_wieferich():
        wieferich = get_wieferich_count()
    else:
        wieferich = read_last_wieferich()


def init_prime():
    """
    initialize prime search program
    :return:
    """
    global prime
    if get_prime_count() > read_last_prime():
        prime = get_prime_count()
    else:
        prime = read_last_prime()