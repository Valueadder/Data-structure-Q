# finding the reversed list
# Naive solutions
l=[2,4,3,5,6]
l1=l.reverse()
l2=list(reversed(l))
l3=l[::-1]



# optimized method
def reverse_element(l):
  s=0
  e=len(l)-1
  while s<e:
    l[s], l[e]=l[e], l[s]
    s+=1
    e-=1
reverse_element(l)
print(l)
    
