def rev_string(str):
  if len(str) == 0:
    return
  if len(str) == 1:
    return str
  return str[-1] + rev_string(str[0:-1])

print(rev_string('abcdefg'))