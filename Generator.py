import random

def GenArray(size):
  a = []
  for _ in range(size):
    a.append(random.randint(-size, size))
  return a

def GenPayload():
  p = []
  sizes = [ 10, 100, 1000, 10000, 100000, 1000000 ]
  for size in sizes:
    p.append(GenArray(size))
  return p 
