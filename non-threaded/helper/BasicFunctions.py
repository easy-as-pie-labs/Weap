# modular exponentiation
def modexp(m, e, n):
    if e == 0:
        return 1
    if e % 2 == 1:
        return modexp(m, e-1, n) * m % n
    else:
        return modexp(m, e//2, n) ** 2 % n


# check if number is composite fermat
def is_composite_fermat(n):
    return modexp(2, n - 1, n) != 1


# check if number is wieferich number
def check_if_wieferich(p):
    return modexp(2, p-1, p**2) == 1
