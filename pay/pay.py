def main():
    h = get_int('Hours Worked: ')
    r = get_float('Pay per Hour: ')

    p = get_pay(h, r)

    print('Total pay is', p)



def get_int(prompt):
    try: return int(input(prompt))
    except: get_int(prompt)

def get_float(prompt):
    try: return float(input(prompt))
    except: get_float(prompt)

def get_pay(h, r):
    if h > 40: return get_advancedpay(h, r)
    else: return get_basicpay(h, r)

def get_basicpay(h, r):
    return h * r

def get_advancedpay(h, r):
    return get_basicpay(h, r) * 1.5



main()