import math

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

def make_string(entry):
    b = [str(i) for i in entry]
    return " ".join(b)

def permutation(array):
    i = len(array) - 1
    j = i
    while array[i-1] > array[i]:
        i -= 1
    if i <= 0:
        return False

    while (array[j] <= array[i-1]) and j >= i:
        j -= 1

    array[i-1], array[j] = array[j], array[i-1]

    array[i:] = array[i:][::-1]

    return array

def rosalind_output(length):
    array = [i for i in range(1,length+1)]

    number_arrangements = math.factorial(len(array))

    print number_arrangements*2**length
    negative_array(array, my_binaries)

    for i in range(number_arrangements-1):
        array = permutation(array)
        negative_array(array, my_binaries)



def negative_array(array, bin_numbers):
    for i in range(len(bin_numbers)):
        current = []
        for j in range(len(bin_numbers[i])):
            current.append(bin_numbers[i][j]*array[j])
        current = make_string(current)
        print current

def main(number):
    my_binaries = binary_numbers(number)
    rosalind_output(number)

number = 2

my_binaries = binary_numbers(number)
rosalind_output(number)
