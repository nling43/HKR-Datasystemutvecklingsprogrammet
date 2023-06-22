

print('Welcome to the Money Bag Transport Calculator (M.B.I.C) \n' +
      '------------------------------------------------------- \n')

bagsType = ['small', 'medium', 'big']
bagCap = [20, 50, 80]
maxBag = [0, 0, 0]
bagValue = [10_000, 30_000, 60_000]

truckSize = 0
value = 0

while(truckSize < 100):
    truckSize = int(input('What is the volume of the truck (>= 100L:) '))

temp = truckSize

while(temp - bagCap[2] >= 0):  # big bag loop
    temp = temp - bagCap[2]
    maxBag[2] += 1

leftovers = truckSize - (maxBag[2] * bagCap[2])
temp = leftovers

while(temp - bagCap[1] >= 0):  # medium bag loop
    temp = temp - bagCap[1]
    maxBag[1] += 1

leftovers = leftovers - (maxBag[1] * bagCap[1])
temp = leftovers

while(temp - bagCap[0] >= 0):  # small loop
    temp = temp - bagCap[0]
    maxBag[0] += 1

leftovers = leftovers - (maxBag[0] * bagCap[0])


for x in range(0, 3):
    value = value + maxBag[x]*bagValue[x]

print('\nPacking Plan \n'
      '------------ \n'
      f'{maxBag[2]} big bags\n'
      f'{maxBag[1]} medium bags\n'
      f'{maxBag[0]} small bags\n'
      '\n'
      f'Space left : {leftovers:<}L\n'
      f'Total Value: {value:<}kr')
