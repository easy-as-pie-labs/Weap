__author__ = 'thomas'

class MathFunctions(object):

    @staticmethod
    def binary(e):
        return bin(e)[2:]

    '''
    modular exponentiation
    '''
    @staticmethod
    def modexp(m, e, n):
        if e == 0:
            return 1
        if e % 2 == 1:
            return MathFunctions.modexp(m, e-1, n) * m % n
        else:
            return MathFunctions.modexp(m, e//2, n) ** 2 % n

    '''
    check if number is composite fermat
    '''
    @staticmethod
    def is_composite_fermat(n):
        return MathFunctions.modexp(2, n - 1, n) != 1

    '''
    check if number is wieferich number
    '''
    @staticmethod
    def is_wieferich(p):
        return MathFunctions.modexp(2, p-1, p**2) == 1
