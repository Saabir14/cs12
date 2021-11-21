def get_int(dialog):
    try:
        print(dialog, end='')
        return int(input())
    except: return get_int(dialog)

def split(a, n):                                    # Function to split an 'a' into 'n' parts that are as even as possible and return the split parts
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def index(array):
    tmp = []
    for i in array: tmp.append(i)
    array = tmp
    for i in range(len(array)):
        array[i] = (i, array[i])
    return array

def binerysearch(array, target):
    if len(array) == 0: return -1
    if type(array[0]) != tuple: array = index(array)

    if len(array) == 1:
        if array[0][1] == target: return array[0][0]
        else: return -1

    for i in split(array, 2):
        if binerysearch(i, target) != -1: return binerysearch(i, target)

    return -1


x = binerysearch(range(get_int('Array size: ')), get_int('Number to searche: '))
if x == -1:
    print('Target not Found')
else:
    print('Target Fount at Index:', x)