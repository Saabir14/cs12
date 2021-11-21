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

def mergesearch(array, target, efficiency=2):     # Efficiency can be incresed but is 2 by default
    if not type(array[0]) == tuple: array = index(array)
    print(array)


print(mergesearch(range(get_int('Array size: ')), get_int('Number to searche: ')))