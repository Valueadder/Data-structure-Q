# In this program we are going to find max sum with k given elements
# Naive solution
# def maxk(arr, k):
#     res = float("-inf")
#     i = 0
#     n = len(arr)
#     while(i+k-1 < n):
#         curr = 0
#         for j in range(k):
#             curr += arr[i+j]
#         res = max(curr, res)
#         i = i+1
#     return res

# optimized solution using sliding window technique
def maxk(arr,k):
  curr=0
  n=len(n)
  for i in range(k):
    curr+=arr[i]
  res=curr
  for j in range(k, n):
    curr= curr+ arr[i]- arr[i-k]
    res=max(curr, res)
  return res 
   


l = [1, 2, 3, 4, 5]
f = 2
print(maxk(l, f))
