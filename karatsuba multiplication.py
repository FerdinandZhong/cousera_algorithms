def karatsuba(x, y):
    """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
    if len(str(x)) == 1 or len(str(y)) == 1:
        return int(x * y)
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n // 2
        print("half n: %d" % nby2)
        a = x // 10 ** (nby2)
        b = x % 10 ** (nby2)
        c = y // 10 ** (nby2)
        d = y % 10 ** (nby2)

        print("four items: {}, {}, {}, {}" .format(a,b,c,d))
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

        # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10 ** (2 * nby2) + (ad_plus_bc * 10 ** nby2) + bd
        print("product: %d" % prod)
        return prod

if __name__ == '__main__':
    x, y = map(int, input().split(','))
    # print(x, y)
    karatsuba(x, y)
