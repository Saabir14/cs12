def get_int(dialog):
    try:
        print(dialog, end='')
        return int(input())
    except: return get_int(dialog)

def lenearsearche(array, target):
    for i in range(len(array)):
        if array[i] == target: return i
    return -1

x = lenearsearche(range(get_int('Array size: ')), get_int('Number to searche: '))
if x == -1:
    print('Target not Found')
else:
    print('Target Fount at Index:', x)