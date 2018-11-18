

def SSort(a):
  b = []
  while(len(a) > 0):
    smallest = a[0]
    for x in a:
      if(x < smallest):
        smallest = x
    b.append(smallest)
    a.remove(smallest)
  return b
