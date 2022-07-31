def largestelement(l):
   if not l:
     return None
   else:
     result=l[0]
     for i in range(1,len(l)):
       if l[i]>result:
         result=l[i]
   return result
#   for x in l:
#     for y in l:
#       if y>x:
#         break
#     else:
#       return x
#   return None

if __name__== "__main__":
  list1=list(map(int, input().split(' ')))   
  print(largestelement(list1))   

