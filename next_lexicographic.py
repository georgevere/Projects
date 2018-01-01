import math

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

def make_string(entry):
    b = [str(i) for i in entry]
    return " ".join(b)

def rosalind_output(length):
    array = [i for i in range(1,length+1)]

    number_arrangements = math.factorial(len(array))

    print number_arrangements
    print make_string(array)

    for i in range(number_arrangements-1):
        array = permutation(array)
        print make_string(array)

def negative_1(length):
    a = 1


def positive_negative(array):
    if all(i < 0 for i in array) == True:
        return True

print positive_negative([-1,-1])






# rosalind_output(6)
