import time
import math

def sum(n, f1, f2):
    sum = 0
    for number in range(n):
        if number % f1 == 0 or number % f2 == 0:
            sum += number
    return sum


# print sum(1000, 3, 5)


# 1 1 2 3
def even_fib_sum(n):
    a = 1
    b = 1
    sum = 0

    while a < n:
        a, b = b, a + b
        if a % 2 == 0:
            sum += a
    return sum


# print even_fib_sum(4000000)

def is_prime(n):
    if n == 1:
        return False
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))

    for number in range(3, int(max_divisor + 1), 2):
        if n % number == 0:
            return False
    return True


# 2
def largest_prime_factor(n):
    max_factor = 2

    number = 2
    while number * number < n:
        if n % number == 0:
            if is_adam(number):
                max_factor = number
        number += 1

    return max_factor


# print largest_prime_factor(600851475143)
def reverse(n):
    return n[::-1]

def is_pal(n):
    word = str(n)
    reverse_word = reverse(word)

    return word == reverse_word


def largest_palindrome(digits):
    max_n = 10 ** digits
    largest = -1
    cache = {}
    for n in range(max_n, 1, -1):
        for m in range (max_n, 1, -1):
            if (n,m) in cache or (m,n) in cache:
                continue
            product = n * m
            if product > largest and is_pal(product):
                largest = product
                cache[(n,m)] = True
            else:
                cache[(n,m)] = False
    return largest

# print largest_palindrome(4)

def passes_range(low, hi, n):
    for number in range(hi, low, -1):
        if n % number != 0:
            return False
    return True

def smallest_multiple(low, hi):
    n = hi

    while not passes_range(low, hi, n):
        n += hi

    return n

# print smallest_multiple(1, 20)

def compute_gcd(x, y):
    if x > y:
        small = y
    else:
        small = x

    for i in range(1, small+1):
        if ((x % i == 0) and (y%i == 0)):
            gcd = i
    return gcd

def euclid_gcd(x, y):
    while y:
        x, y = y, x % y
        print x, y
    return x

print euclid_gcd(60, 48)