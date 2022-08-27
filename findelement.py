# this program find the all index of given pattern in the string
s = input("Enter the text:\n")
pat = input("Enter the pattern for finding it's index:")
pos = s.find(pat)
while pos >= 0:
    print(pos)
    pos = s.find(pat, pos+1)
