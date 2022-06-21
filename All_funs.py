import math

def max_num(*args):
  max = args[0]
  for i in range(1, len(args)):
    if args[i] > max:
      max = args[i]
  return max
print(max_num(1, 20, 3))

def mult_list(the_list):
  value = 1
  for i in the_list:
    value = value * i
  return value
print(mult_list([2, 3, 4]))

def rev_string(str):
  if len(str) == 0:
    return
  if len(str) == 1:
    return str
  return str[-1] + rev_string(str[0:-1])
print(rev_string('abcdefg'))

def num_within(number, beginning, end):
  if number >= beginning and number <= end:
    return True
  return False
print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

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