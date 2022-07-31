def largestelement(l):
  for x in l:
    for y in l:
      if y>x:
        break
    else:
      return x
  return None

if __name__== "__main__":
  list1=list(map(int, input().split(' ')))   
  print(largestelement(list1))     
