# modular exponentiation
def modexp(m, e, n):
    if e == 0:
        return 1
    if e % 2 == 1:
        return modexp(m, e-1, n) * m % n
    else:
        return modexp(m, e//2, n) ** 2 % n

# check if number is composite fermat
def isCompositeFermat(n):
    return modexp(2, n - 1, n) != 1

if __name__ == "__main__":
    m = 123234
    e = 235623
    n = 8239234
    print modexp(m, e, n)
    print isCompositeFermat(561)