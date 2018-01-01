def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n>1:
        primfac.append(n)
    return primfac

for i in range(1, 151):
    if 2 not in primes(i):
        print i, primes(i), 1/float(i)
