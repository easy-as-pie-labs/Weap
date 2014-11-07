from __future__ import print_function
from BasicFunctions import *
import os

__author__ = 'goggelz'

prime = 1
wieferich = 1

def write_prime(p):
    f = open('primes.txt', 'a')
    print(p, file=f)
    f.close()


def write_wieferich(w):
    f = open('wieferichs.txt', 'a')
    print(w, file=f)
    f.close()


def set_prime_counter(p):
    f = open('counterPrime.txt', 'a')
    print(p, file=f)
    f.close()


def set_wieferich_counter(w):
    f = open('counterWieferichs.txt', 'a')
    print(w, file=f)
    f.close()


def create_wieferichs():
    global wieferich
    while True:
        wieferich += 2
        if check_if_wieferich(wieferich):
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
    if not os.path.isfile('primes.txt'):
        open('primes.txt', "a").close()

    f = open('primes.txt', "r")

    last = f.readlines()
    f.close()
    if last:
        prime = long(last[-1])+2
    return prime


def read_last_wieferich():
    global wieferich
    if not os.path.isfile('wieferichs.txt'):
        open('wieferichs.txt', "a").close()

    f = open('wieferichs.txt', "r")

    last = f.readlines()
    f.close()
    if last:
        wieferich = long(last[-1])+2
    return wieferich

def get_prime_counter():
    global prime
    if not os.path.isfile('counterPrime.txt'):
        open('counterPrime.txt', "a").close()
    f = open('counterPrime.txt', "r")

    last = f.readlines()
    f.close()
    if last:
        prime = long(last[-1])+2
    return prime

def get_wieferich_counter():
    global wieferich
    if not os.path.isfile('counterWieferichs.txt'):
        open('counterWieferichs.txt', "a").close()
    f = open('counterWieferichs.txt', "r")

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