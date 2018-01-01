def binary_numbers(a):
    alist = []

    digits = a
    numbers = 2**digits-1

    for i in range(numbers+1):
        a = list(bin(i))
        a = a[2:][::-1]
        for i in range(digits-len(a)):
            a.append(0)
        for i in range(len(a)):
            a[i] = int(a[i])
        alist.append(a[::-1])

    for i in alist:
        for j in range(len(i)):
            if i[j] == 0:
                i[j] = -1

    return alist


print binary_numbers(2)
