def max_num(*args):
  max = args[0]
  for i in range(1, len(args)):
    if args[i] > max:
      max = args[i]
  return max

print(max_num(1, 20, 3))