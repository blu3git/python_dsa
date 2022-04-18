# Greatest Common Divisor

def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)

print(find_gcd(8,12))