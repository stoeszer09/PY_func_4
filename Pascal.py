import math

def pascal(num):
  if num < 1:
    print('Wrong number')
    return
  row = ''
  for i in range(0, num):
    for j in range(0, i + 1):
      row = row + str(math.comb(i, j)) + ' '
    print(row)
    row = ''

pascal(5)