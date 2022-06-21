from operator import truediv


def num_within(number, beginning, end):
  if number >= beginning and number <= end:
    return True
  return False

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))