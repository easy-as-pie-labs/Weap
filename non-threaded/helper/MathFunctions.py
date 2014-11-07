__author__ = 'thomas'

class MathFunctions(object):

    @staticmethod
    def modexp(m, e, n):
        """
        modular exponentiation
        :param m: ?
        :param e: ?
        :param n: ?
        :return:
        """
        if e == 0:
            return 1
        if e % 2 == 1:
            return MathFunctions.modexp(m, e-1, n) * m % n
        else:
            return MathFunctions.modexp(m, e//2, n) ** 2 % n

    @staticmethod
    def is_composite_fermat(n):
        """
        check if number is composite fermat
        :param n: number to check
        :return: True or False
        """
        return MathFunctions.modexp(2, n - 1, n) != 1

    @staticmethod
    def is_wieferich(p):
        """
        check if number is wieferich number
        :param p: number (usually prime) to check
        :return: True or False
        """
        return MathFunctions.modexp(2, p-1, p**2) == 1
