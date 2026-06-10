import math

# For finding the sum of all prime numbers up to an upper bound, we can use Eratosthenes' sieve algorithm
# We can create a boolean array where the indices represent a sequence of numbers
# We essentially mark all multiples of each number as not prime
# At the end, we search through the list for all prime numbers left and take their sum


def sum_of_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    sum = 0

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    for k in range(0, limit):
        if is_prime[k]:
            sum += k
    
    return sum

result = sum_of_primes(2000000)

print(result)