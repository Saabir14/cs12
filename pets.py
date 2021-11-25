def get_char(prompt=''):
    x = input(prompt)
    if len(x) != 1: return get_char(prompt)
    else: return x

array = [[(input('Owner Name: ')), input('Pet Type: ')]]
print(array)

x = get_char('1.\tAdd another owner and pet\n2.\tChange/Amend an owner/pet\n3.\tAdd new owner and pet\n4.\tPrint the list of owners and pets\n\nChoose: ')
if x == 1: array.append([(input('Owner Name: ')), input('Pet Type: ')])
elif x == 2:
    array[input('Index: ')] = [(input('Owner Name: ')), input('Pet Type: ')]
elif x == 3: array.append([(input('Owner Name: ')), input('Pet Type: ')])
elif x == 4: print(array)