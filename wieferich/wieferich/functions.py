__author__ = 'Janneck'


# modulare Exponentation
def modexp(m, e, n):
    if e == 0:
        return 1
    if e % 2 == 1:      # e ungerade
        return modexp(m, e-1, n)*m % n
    else:
        return modexp(m, e//2, n)**2 % n


# wieferichtest
def iswieferich(p):
    return modexp(2, p-1, p**2) == 1

i = 10**17 + 1

while 1 == 1:
    i += 2
    if iswieferich(i):
        print i
    if i % 100000 == 1:
        print "control: " + str(i)
