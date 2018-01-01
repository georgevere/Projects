def population(k, m, n):

    k = float(k)
    m = float(m)
    n = float(n)

    t = k + m + n

    probability = ((k*k) - k + (2*k*m) + (2*k*n) + (0.75*m*m) - (0.75*m) + (m*n))/(t*(t-1))

    return probability

print population(25,16,17)
