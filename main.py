import timeit
from SelectionSort import SSort
from MergeSort import MSort
from QuickSort import QSort
from Generator import GenArray

a = [ 5, 29, -32, 47, 6 ]
b = [ 4, 4, 4, 4, 4, 4, 5 ]
c = GenArray()

def wrapper(func, *args, **kwargs):
  def wrapped():
    return func(*args, **kwargs)
  return wrapped

#QSort(a,0,len(a)-1)
#print(a)
#QSort(b,0,len(b)-1)
#print(b)
#QSort(c,0,len(c)-1)
#print(c)
wrapped = wrapper(SSort,a)
print(timeit.timeit(wrapped, number=1))
wrapped = wrapper(SSort,b)
print(timeit.timeit(wrapped, number=1))
wrapped = wrapper(SSort,c)
print(timeit.timeit(wrapped, number=1))
wrapped = wrapper(MSort,a)
print(timeit.timeit(wrapped, number=1))
wrapped = wrapper(MSort,b)
print(timeit.timeit(wrapped, number=1))
wrapped = wrapper(MSort,c)
print(timeit.timeit(wrapped, number=1))

