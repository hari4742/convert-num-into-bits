def countbits(x):
    y = 2
    quotient = x//y
    power = 0
    bits = {}
    while True:
        if x == 0:
            break
        elif quotient > 1:
            y *= y
            power += 1
        elif quotient == 1:
            x = x % y
            power += 1
            bits[power]=1
            power = 0
        else:
            bits[power] = 1
            break
    list = []
    for i in range(9):
        list.append (power.get(i,0))
    return list
print(countbits(15))
