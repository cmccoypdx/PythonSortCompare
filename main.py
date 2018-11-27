import copy
import random
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
MArray = copy.deepcopy(PayloadArray)
QArray = copy.deepcopy(PayloadArray)
MDict = benchmark(MSort, MArray)
QDict = benchmark(QSort, QArray)

SDict = {k : v / 10 for k, v in SDict.items()}
MDict = {k : v / 10 for k, v in MDict.items()}
QDict = {k : v / 10 for k, v in QDict.items()}

print(SDict)
print(MDict)
print(QDict)

arand = random.randint(0,9)
print(arand)
srand = random.randint(0,3)
print(srand)
brand = random.randint(0,6)
print(brand)

ss = SmallPayloadArray[arand][srand]
ms = MArray[arand][brand]
qs = QArray[arand][brand]

if (all(ss[i] <= ss[i+1] for i in range(len(ss)-1))):
  print("Sorted")
else:
  print("Not sorted")
if (all(ms[i] <= ms[i+1] for i in range(len(ms)-1))):
  print("Sorted")
else:
  print("Not sorted")
if (all(qs[i] <= qs[i+1] for i in range(len(qs)-1))):
  print("Sorted")
else:
  print("Not sorted")

