# find the second largest element in the list
# Naive Solution
def largestelement(l):
     result=l[0]
     for i in range(1,len(l)):
       if l[i]>result:
         result=l[i]
     return result

def secLargest(l):
  if len(l)<=1:
    return None
  lar=largestelement(l)
  slar=None
  for i in l:
    if i!=lar:
      if slar==None:
        slar=i
      else:
        slar=max(slar,i)
  return slar

# optimized solution
def secLargest(l):
  if len(l)<=1:
    return None
  lar=l[0]
  slar=None
  for i in l[1:]:
    if i>lar:
      slar=lar
      lar=i
    elif i!=lar:
      if slar==None or slar<i:
        slar=i
  return slar      

l=[3,24,6,45,67]
sl=secLargest(l)
print(sl)





  