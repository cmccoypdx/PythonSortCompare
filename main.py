import copy
from SelectionSort import SSort
from MergeSort import MSort
from QuickSort import QSort
from Generator import GenArray
from Generator import GenPayload
from Timer import TimeFunc 

c = GenArray(10)
d = GenPayload()

def benchmark(alg, payload):
  for arr in payload:
    print(len(arr))
    print(TimeFunc(alg, arr))

benchmark(SSort, copy.deepcopy(d[0:4]))
benchmark(MSort, copy.deepcopy(d))
benchmark(QSort, copy.deepcopy(d))
#print(d[0:4])

#print(TimeFunc(MSort, copy.deepcopy(c)))
#print(TimeFunc(QSort, copy.deepcopy(c),0,len(c)-1))
