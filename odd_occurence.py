# given a list we have to find elements with odd occurence 
def odd_element(l):
  res=None
  for i in l:
    count=l.count(i)
    if count%2!=0:
      res=i
      break
  return res

#optimized approach with bitwise XOR 
def odd_bitwise(l):
  res=0
  for i in l:
    res=res^i
  return res  


if __name__=="__main__":
  l= [2, 4, 5, 4, 2, 7, 5]    
  print(odd_bitwise(l))