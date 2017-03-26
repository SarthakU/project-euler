from math import sqrt
from math import ceil

def biggest_factor(n):
    comps = 0
    for i in range(3, ceil(sqrt(n + 1)), 2):
        if n % i == 0:
            return int(n / i)

if __name__ == "__main__":
    number = 600851475143
    print(biggest_factor(number))
