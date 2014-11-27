# coding=utf-8
__author__ = 'TPei'
import math
import numpy as np
import datetime

start_time = datetime.datetime.today()

'''
funktioniert der variable Anfang so???

zahlenbereich der ueberprueft wird... ich will wissen wie lang es dauert 12.8 Millionen Primzahlen zu finden
14540703
'''
end = 12800000*10
start = end - (end/10)
gestrichen = np.zeros(end, dtype=bool)
primes = []
print len(gestrichen)

for i in range(start, end):
    if not gestrichen[i]:
        primes.append(i)

        for j in range(i*i, end, i):
            gestrichen[j] = True

for i in range(max(start, int(math.sqrt(end))+1), end):
    if not gestrichen[i]:
        primes.append(i)

print len(primes)
print datetime.datetime.today() - start_time

