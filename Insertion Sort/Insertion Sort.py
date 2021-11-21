def get_int(dialog):
    try:
        print(dialog, end='')
        return int(input())
    except: return get_int(dialog)

def insertionsort(array):
    if len(array) == 1: return array
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            # Find Position and switche
            for j in range(len(array)):
                if array[i] < array[j]:
                    array.insert(j, array.pop(i))
                    break
            array = insertionsort(array)
            break


array = []
for i in range(get_int('Array size: ')):
    array.append(get_int(f'Index {i}: '))

insertionsort(array)
print(array)