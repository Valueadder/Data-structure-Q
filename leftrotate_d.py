# Naive solution for left rotate a list by d(given) places
# l=[1,2,3,4,5,6,7]
# d=2
# l= l[d:] + l[:d]
# print(l)
# In this solution worst case is O(n) but in this auxilary space is more

# Using deque
# from collections import deque
# l=[1,2,3,4,5,6,7]
# d=2
# dq=deque(l)
# dq.rotate(-d)
# l=list(dq)
# print(l)

# optimized solution using reverse
def reverse(l, s, e):
    while s<e:
        l[s], l[e] = l[e], l[s]
        s = s+1
        e = e-1


def leftrotate_d(l, d):
    n = len(l)
    reverse(l, 0, d-1)
    reverse(l, d, n-1)
    reverse(l, 0, n-1)


list1 = [1, 2, 3, 4, 5, 6, 7]
leftrotate_d(list1, 3)
print(list1)
