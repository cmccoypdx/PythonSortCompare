"""Module for holding selection sort algorithm"""

def SSort(a):

  """Returns sorted list with contents of input list. 
   Does not modify input list"""

  b = []
  c = list(a)        # make copy of a
  while(len(c) > 0):
    smallest = c[0]
    for x in c:
      if(x < smallest):
        smallest = x
    b.append(smallest)
    c.remove(smallest)
  return b
