"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        print("loop2")
        n: float = n / i
        print(n)
    i: int = i + 1

print(n)
