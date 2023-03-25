# program to find the binary conversion of a given number

def convert_binary(n):
    if n == 0:
        return
    convert_binary(n//2)
    print(n % 2)


if __name__ == "__main__":
    n = int(input("Enter the number to find binary representation:\n"))
    convert_binary(n)
