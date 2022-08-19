# this program is to find the given sum is present in array or not
#  Naive solution 
# def subsum(arr, sume):
#   for i in range(len(arr)):
#     curr=0
#     for j in range(i, len(arr)):
#       curr+=arr[j]
#       if curr==sume:
#         return True
#   return False

#optimized solution
#   

if __name__== "__main__":
  l=[2, 4, 5, 6, 7]
  k=9
  v=subsum(l, k)
  print(v)       
