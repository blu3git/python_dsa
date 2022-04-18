
def recursive_range(n):
    if n == 0:
        return n
    return n + recursive_range(n-1)

print(recursive_range(10))