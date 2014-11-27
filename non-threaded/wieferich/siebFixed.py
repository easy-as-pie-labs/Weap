__author__ = 'TPei'
import math
import numpy as np
import datetime

start_time = datetime.datetime.today()

'''
hier wird von 2 gestartet, muss entsprechend angepasst werden
zahlenbereich der ueberprueft wird... ich will wissen wie lang es dauert 12.8 Millionen Primzahlen zu finden
'''
N = 12800000*10
gestrichen = np.zeros(N, dtype=bool)
primes = []
print len(gestrichen)

for i in range(2, N):
    if not gestrichen[i]:
        primes.append(i)

        for j in range(i*i, N, i):
            gestrichen[j] = True

for i in range(int(math.sqrt(N))+1, N):
    if not gestrichen[i]:
        primes.append(i)

print len(primes)
print datetime.datetime.today() - start_time

