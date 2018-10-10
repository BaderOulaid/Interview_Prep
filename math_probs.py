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

# print euclid_gcd(60, 48)

def sum_square_difference(n):
    sum = 0
    sum_sq = 0
    for number in range(1, n+1):
        sum += number
        sum_sq += number ** 2
    return sum ** 2 - sum_sq

# print sum_square_difference(100)


def nth_prime(n):
    i = 2
    while n > 0:
        if is_prime(i):
            n -= 1
        i += 1
    return i - 1


# print nth_prime(10001)

def linearSearch(digits, k):
    l = 0; #non 0 digits from last 0 we found
    prod = 1

    maxProd = 0

    for i in range(0,len(str(digits))): # for each index of digits
        prod*=int(str(digits)[i]) # we multiply the accumulative product by the digit at position i
        l+=1 # we add 1 to consecutive non 0
        if int(str(digits)[i]) == 0: # if its actually a 0, we reset both length and prod
            l=0
            prod = 1
        if l >= k: # we have found at least k non 0 consecutive digits
            maxProd = max(maxProd,prod) # store max between maxValue and newValue
            prod/=int(str(digits)[i-k+1]) # we remove the last digit from the product with division, so prod now has k-1 digits multiplications

    return maxProd

print linearSearch(9456, 2)
