from __future__ import print_function
from MathFunctions import *
import os

'''
TODO:
put this in a class or whatever as a wrapper
add comments
'''

__author__ = 'goggelz'

prime = 1
wieferich = 1

'''
file name constants
'''
PRIMES_FILE = 'primes.txt'
WIEFERICHS_FILE = 'wieferichs.txt'
PRIME_COUNTER_FILE = 'counterPrime.txt'
WIEFERICHS_COUNTER_FILE = 'counterWieferichs.txt'


def write_to_file(filename, value):
    f = open(filename, 'a')
    print(value, file=f)
    f.close()


def write_prime(prime_to_save):
    write_to_file(PRIMES_FILE, prime_to_save)


def write_wieferich(wieferich_to_save):
    write_to_file(WIEFERICHS_FILE, wieferich_to_save)


def set_prime_counter(p):
    f = open(PRIME_COUNTER_FILE, 'a')
    print(p, file=f)
    f.close()


def set_wieferich_counter(w):
    f = open(WIEFERICHS_COUNTER_FILE, 'a')
    print(w, file=f)
    f.close()


def find_wieferichs():
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
    global wieferich
    if not os.path.isfile(WIEFERICHS_FILE):
        open(WIEFERICHS_FILE, "a").close()

    f = open(WIEFERICHS_FILE, "r")

    last = f.readlines()
    f.close()
    if last:
        wieferich = long(last[-1])+2
    return wieferich


def get_prime_counter():
    global prime
    if not os.path.isfile(PRIME_COUNTER_FILE):
        open(PRIME_COUNTER_FILE, "a").close()
    f = open(PRIME_COUNTER_FILE, "r")

    last = f.readlines()
    f.close()
    if last:
        prime = long(last[-1])+2
    return prime


def get_wieferich_counter():
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
    global wieferich
    if get_wieferich_counter() > read_last_wieferich():
        wieferich = get_wieferich_counter()
    else:
        wieferich = read_last_wieferich()


def init_prime():
    global prime
    if get_prime_counter() > read_last_prime():
        prime = get_prime_counter()
    else:
        prime = read_last_prime()