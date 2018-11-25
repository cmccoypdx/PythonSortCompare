import random

def HPart(a,l,r):
  p = a[l]
  i = l
  j = r + 1
  while(i < j):
    i += 1
    j -= 1
    while(i < len(a) and a[i] < p):
      i += 1
    while(j > 0 and a[j] > p):
      j -= 1
    if(i < len(a) and j > 0):
      a[i], a[j] = a[j], a[i]

  if(i < len(a) and j > 0):
    a[i], a[j] = a[j], a[i]
  a[l], a[j] = a[j], a[l]
  return j

def QSort(a,l,r):
  if(l < r):
    s = HPart(a,l,r)
    QSort(a,l,s-1)
    QSort(a,s+1,r)
