power = 0
bits = {}
x = 9
y = 2
quotient = x//y
while True:
    if x == 0:
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
for i in range(9):
    list.append (bits.get(i,0))
list.reverse()
firstoccur = list.index(1)
print(list)
print("finished")
print(list.count(1))


