def pkString(k, s):
    # write your code here
    result = 0
    l = list(s.split(''))
    for i in l:
        if (i == 'p'):
          if int(l.index(i)) == k:
            result = 1
        else:
            result = 0
    return result


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = int(input())
        s = input()
        pkString(k, s)
