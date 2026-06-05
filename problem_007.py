import math

# We can use the formula n * ln(n * ln(n)) to find the approximate upper bound of our search
# By using Eratosthenes' sieve algorithm, we can collect all prime numbers up to our limit into a list
# At the end, we simply need to search for the prime number at the position number in the list

def findPrime(position):
    primes_list = [2, 3]
    limit = position * math.log(position * math.log(position))
    for i in range(4, 115000):
        for x in primes_list:
            if i % x == 0:
                flag = False
                break
            flag = True
        if flag == True:
            primes_list.append(i)
    return primes_list[position - 1]

result = findPrime(10001)
print(result)
        
