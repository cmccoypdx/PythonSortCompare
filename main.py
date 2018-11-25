import copy
from SelectionSort import SSort
from MergeSort import MSort
from QuickSort import QSort
from Generator import GenArray
from Timer import TimeFunc 

a = [ 5, 29, -32, 47, 6 ]
b = [ 4, 4, 4, 4, 4, 4, 5 ]
c = GenArray()

print(TimeFunc(SSort, a))
print(TimeFunc(SSort, b))
print(TimeFunc(SSort, c))
print(TimeFunc(MSort, copy.deepcopy(a)))
print(TimeFunc(MSort, copy.deepcopy(b)))
print(TimeFunc(MSort, copy.deepcopy(c)))
print(TimeFunc(QSort, copy.deepcopy(a),0,len(a)-1))
print(TimeFunc(QSort, copy.deepcopy(b),0,len(b)-1))
print(TimeFunc(QSort, copy.deepcopy(c),0,len(c)-1))
