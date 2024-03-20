#general test

def front_back(str):
  if len(str) <= 1:
    return str
  elif len(str) == 2:
    return str[1]+str[0]
  first = str[0]
  mid = str[1:-1]
  last = str[-1]
  return last+mid+first

print(front_back("ab"))