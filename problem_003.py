# We can use the trial division algorithm where we continuously divide our given number by odd numbers up to its square root
# First, we need to check if the number is even and then continuously divide by 2 until it is odd
# Then, we can divide our number by each term in a sequence of odd numbers starting from 3
# If the term is divisible, then we perform the division operation
# The second-last divisor recorded will be our largest prime factor


def greatest_prime_factor(number: int) -> int:
    divisor = 3

    while (number % 2 == 0):
        number = number / 2
    
    while (number > 1):
        if (number % divisor == 0):
            number = number / divisor
        divisor += 2
    # subtracting the return value by 2 because we added an extra 2 on the last iteration
    return divisor - 2

result = greatest_prime_factor(600851475143)

print(result)
        
        