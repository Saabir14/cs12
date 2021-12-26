def get_int(dialog):
    try:
        print(dialog, end='')
        return int(input())
    except: return get_int(dialog)

def split(a, n):                                    # Function to split an 'a' into 'n' parts that are as even as possible and return the split parts
    k, m = divmod(len(a), n)
    return list((a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)))

def index(array):
    tmp = []
    for i in array: tmp.append(i)
    array = tmp
    for i in range(len(array)):
        array[i] = (i, array[i])
    return array

def binarysearch(array, target):
    if len(array) == 0: return -1
    if type(array[0]) != tuple: array = index(array)

    if len(array) == 1:
        if array[0][1] == target: return array[0][0]
        else: return -1

    slicedarray = split(array, 2)
    if slicedarray[1][0][1] > target:
        a = binarysearch(slicedarray[0], target)
        if a != -1: return a
    else:
        a = binarysearch(slicedarray[-1], target)
        if a != -1: return a

    return -1


array = range(get_int('Array Size: '))
x = binarysearch(array, get_int('Number to searche: '))

if x == -1:
    print('Target not Found')
else:
    print('Target Fount at Index:', x)