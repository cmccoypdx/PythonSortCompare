from SelectionSort import SSort
from MergeSort import MSort
from QuickSort import QSort

a = [ 5, 29, -32, 47, 6 ]
b = [ 4, 4, 4, 4, 4, 4, 5 ]

QSort(a,0,len(a)-1)
print(a)
QSort(b,0,len(b)-1)
print(b)
print(SSort(a))
print(SSort(b))
#print(MSort(a))
#print(MSort(b))
