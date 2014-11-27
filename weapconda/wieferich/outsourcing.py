@cuda.jit('void(uint64[:], uint64[:])', target='gpu')
def checkwieferich(check, result):
    """
    checks if a given number is a wieferich prime
    :param check: list of numbers to check
    :param result: list of wieferich numbers (or 0)
    :return:
    """
    #current index
    i = cuda.grid(1)
    ac = check[i]

    #modexp params
    m = 2
    e = ac-1
    n = ac**2

    if modexp(m, e, n) == 1:
        result[i] = ac





@cuda.jit('uint64(uint64)', inline=True, device=True)
def inline_wieferich(ac):
    m = 2
    e = ac-1
    n = ac**2

    if modexp(m, e, n) == 1:
        return ac
    return 0





@cuda.jit('void(uint64[:], uint64[:])', target='gpu')
def fermat_wieferich(check, result):
    """
    checks if a given number is composite fermat
    :param check: list of numbers to check
    :param result: list of composite fermats numbers (or 0)
    :return:
    """
    #current index
    i = cuda.grid(1)
    ac = check[i]

    #params for fermat-check
    m = 2
    e = ac-1
    n = ac

    #if fermat run wieferich-check
    if modexp(m, e, n) != 1:
        result[i] = inline_wieferich(ac)

