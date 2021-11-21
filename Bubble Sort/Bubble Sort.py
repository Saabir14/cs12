def get_int(dialog):
    try:
        print(dialog, end='')
        return int(input())
    except: return get_int(dialog)

def bubblesort(array):
    if len(array) == 1: return array
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            array[i], array[i - 1] = array[i - 1], array[i]
            array = bubblesort(array)
            break


array = []
for i in range(get_int('Array size: ')):
    array.append(get_int(f'Index {i}: '))

bubblesort(array)
print(array)