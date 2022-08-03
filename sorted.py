# naive solution
def is_Sorted(l):
  i=1
  while i<len(l):
    if l[i]<l[i-1]:
      return False
    i=i+1
  return True
if __name__=="__main__":
  l=[10,20,30,40]
  if is_Sorted(l):
    print("Yes")
  else:
    print("No")  

