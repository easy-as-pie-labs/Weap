__author__ = 'local admin'



def recursive_modexp(m, e, n):
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
            return recursive_modexp(m, e-1, n) * m % n
        else:
            return recursive_modexp(m, e//2, n) ** 2 % n