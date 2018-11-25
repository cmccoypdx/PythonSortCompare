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

def qSort(a,l,r):
  if(l < r):
    s = HPart(a,l,r)
    qSort(a,l,s-1)
    qSort(a,s+1,r)

def QSort(a):
  qSort(a, 0, len(a)-1)
