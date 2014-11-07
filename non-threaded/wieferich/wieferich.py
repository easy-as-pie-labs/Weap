from helper.BasicFunctions import *

def check_if_wieferich(p):
    return modexp(2, p-1, p**2) == 1

if __name__ == '__main__':
    i = 10**17 + 1

    while True:
        i += 2
        if check_if_wieferich(i):
            print i
        if i % 100000 == 1:
            print "control: " + str(i)
