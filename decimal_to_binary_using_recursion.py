def convert(n):
    if n == 0:
        return n
    return n%2 + 10 * convert(int(n/2))

print(convert(10))