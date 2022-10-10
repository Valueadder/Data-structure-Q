# this program finds the given both strings have same elements or not despite having different orders
# naive solution (time complexity: O(nlogn))
# def anagram(s1, s2):
#   if len(s1)!=len(s2):
#     return False
#   s1=sorted(s1)
#   s2=sorted(s2)
#   if s1==s2:
#     return True
#   else:
#     return False

# optimized solution (time complexity(O(n)))
def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = [0]*256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    for x in count:
        if x != 0:
            return False
    return True


if __name__ == "__main__":
    s1 = input("Enter the string:\n")
    s2 = input("Enter the string to find:\n")
    print(anagram(s1, s2))
