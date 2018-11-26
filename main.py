import copy
from SelectionSort import SSort
from MergeSort import MSort
from QuickSort import QSort
from Generator import GenPayload
from Timer import TimeFunc 

def benchmarkPass(alg, payload):
  ndict = {
      10       : 0.0,
      100      : 0.0,
      1000     : 0.0,
      10000    : 0.0,
      100000   : 0.0,
      1000000  : 0.0,
      10000000 : 0.0
    }

  for arr in payload:
    ndict[len(arr)] = TimeFunc(alg, arr)

  return ndict

def benchmark(alg, parr):
  ndict = {
      10       : 0.0,
      100      : 0.0,
      1000     : 0.0,
      10000    : 0.0,
      100000   : 0.0,
      1000000  : 0.0,
      10000000 : 0.0
    }

  for payload in parr:
    tempdict = benchmarkPass(alg, payload)
    for n in tempdict:
      ndict[n] += tempdict[n]
  return ndict

PayloadArray = []
SmallPayloadArray = []
for _ in range(10):
  p = GenPayload()
  PayloadArray.append(p)
  SmallPayloadArray.append(p[0:4])

SDict = benchmark(SSort, SmallPayloadArray)
MDict = benchmark(MSort, copy.deepcopy(PayloadArray))
QDict = benchmark(QSort, copy.deepcopy(PayloadArray))

SDict = {k : v / 10 for k, v in SDict.items()}
MDict = {k : v / 10 for k, v in MDict.items()}
QDict = {k : v / 10 for k, v in QDict.items()}

print(SDict)
print(MDict)
print(QDict)
  
