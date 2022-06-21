def mult_list(the_list):
  value = 1
  for i in the_list:
    value = value * i
  return value

print(mult_list([2, 3, 4]))