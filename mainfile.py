def convert_bits(x):
    y = 2
    quotient = x//y
    power = 0
    bits = {}
    while True:
        if x <= 0:
            break
        elif quotient > 1:
            y *= 2
            power += 1
            quotient = x//y
        elif quotient == 1:
            x = x % y
            power += 1
            bits[power]=1
            power = 0
            y = 2
            quotient = x//y
        else:
            bits[power] = 1
            break
    list = []
    for i in range(50):
        list.append (bits.get(i,0))
    list.reverse()
    first = list.index(1)
    newlist = list[first:]
    newlist.reverse()
    return newlist

num = int(input("enter a number: "))
if num <=0:
    print("plese enter a positive integer")

try:
    print(convert_bits(num))
    print("hi")
except:
    print("finished!")


