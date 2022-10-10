# this program will find the given pattern in given string
# Naive solution
# def naivepat(txt, pat):
#     m = len(pat)
#     n = len(txt)
#     for i in range(n-m+1):
#         j = 0
#         while j < m:
#             if pat[j] != txt[i+j]:
#                 break
#             j += 1
#         if j == m:
#             print(i, end=" ")

# Suppose if pattern given by user is distinct
def distinctpat(txt, pat):
    n = len(txt)
    m = len(pat)
    i = 0
    while i <= n-m:
        for j in range(0, m):
            if pat[j] != txt[i+j]:
                break
            j += 1  # this is not given in the course ask doubt
        if j == m:
            print(i, end=" ")
        if j == 0:
            i = i+1
        else:
            i = i+j


s1 = input("Enter the text:\n")
s2 = input("Enter the pattern:\n")
distinctpat(s1, s2)
