# Program to find whether a string is palindrome or not
s = input("Enter the string:")
low = 0
high = len(s)-1
while low < high:
    if s[low] != s[high]:
        print("No")
        break
    low += 1
    high -= 1
else:
    print("Yes")

# simple solution
rev = s[::-1]
if s == rev:
    print("Yes")
else:
    print("No")
