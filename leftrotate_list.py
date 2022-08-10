# Naive solution to left rotate an element by one place
l=[1,2,3,4,5,6]
# n=len(l)
# l=l[1:n] + l[0:1]
# print(l)
# l.append(l.pop(0))
# print(l)

# optimized solution
def left_rotate(l):
  x=l[0]
  n=len(l)
  for i in range(1,n):
    l[i-1]=l[i]
  l[n-1]=x 

left_rotate(l)
print(l)   
