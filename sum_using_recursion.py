
def sum_of_digits(n):
    if n == 0:
        return n
    return int(n%10) + sum_of_digits(int(n/10))

print(sum_of_digits(1112))