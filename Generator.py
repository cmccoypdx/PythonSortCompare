import random

def GenArray():
  a = []
  for _ in range(10000):
    a.append(random.randint(-10000,10000))
  return a
