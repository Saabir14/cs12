def get_int(prompt):
    try: return(int(input(prompt)))
    except: return(get_int(prompt))

def get_num(prompt, max=0, min=0):
    x = get_int(prompt)
    if x <= max and x >= min: return x
    else: return get_num(prompt, max, min)

array = [[(input('Owner Name: ')), input('Pet Type: ')]]

while True:
    x = get_int('1.\tAdd another owner and pet\n2.\tChange/Amend an owner/pet\n3.\tAdd new owner and pet\n4.\tPrint the list of owners and pets\n5.\tBreak and save to file\n\nChoose: ')
    if x == 1: array.append([(input('Owner Name: ')), input('Pet Type: ')])
    elif x == 2:
        y = get_num('Index: ', min=0, max=len(array) - 1)
        array[y] = [(input('Owner Name: ')), input('Pet Type: ')]
    elif x == 3: array.append([(input('Owner Name: ')), input('Pet Type: ')])
    elif x == 4: print(array)
    else: break

with open('Customer.txt', 'w') as file:
    for i in array:
        file.write(i[0] + ', ' + i[1] + '\n')