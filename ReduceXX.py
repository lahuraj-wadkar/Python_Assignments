from functools import reduce

chkEven = lambda no:(no%2==0)

Inclrement = lambda no:(no+1)

Addition = lambda no1, no2: (no1 + no2)
  
def main():
  Data = [1,3,2,5 7,10]
  fData = list(filter(chkEven, Data))
  print("Data after fitler:", fData)
  MData = list(map(Increment, fData))
  print("Data after map:", MData)
  rData = reduce(Addition,  MData)
  print("Data after reduce :", rData)
  
if(__name__ == "__main__"):
  main()
