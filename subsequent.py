# program to find a text inside a string in same sequence as it given
def subsequence(s1, s2):
    if len(s1) < len(s2):
        return False
    else:
        i, j = 0, 0
        while (i < len(s1) and j < len(s2)):
            if s1[i] == s2[j]:
                j = j+1
            i = i+1
        if j == len(s2):
            return True
        else:
            return False


s1 = input("Enter the raw string:")
s2 = input("Enter the string to find:")
print(subsequence(s1, s2))
