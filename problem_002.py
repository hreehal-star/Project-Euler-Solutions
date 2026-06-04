import math

# Approach 1:
# We can simply iterate through the sequence and add each even term to the sum

# Approach 2:
# We can use Binet's formula to calculate each fibonacci number in the sequence
# Since the sequence follows a pattern of an even number followed by two odd numbers and then an even number again, we can calculate only the even numbers
# Our sequence will be 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# We will use zero-based indexing so we only need to calculate the terms at positions 0, 3, 6, 9, 12, ...

def even_fibonacci(upper_bound: int):
    sigma = (1 + math.sqrt(5)) / 2.0
    tau = (1 - math.sqrt(5)) / 2.0
    sum = 0
    term = 0
    i = 0

    while (True):
        term = ((sigma ** i) - (tau ** i)) / math.sqrt(5)
        if term > upper_bound:
            break
        sum += int(term)
        i += 3

    return sum

result = even_fibonacci(4000000)
print(result)

# Below is the brute force solution that iterates through all terms in the sequence
'''
def fibonacci(upper_bound):
    n1 = 2
    n2 = 3
    sum = 2
    i = 0
    while (i < upper_bound):
        if (i % 2 == 0):
            sum += i
        fast = fast + slow
        slow = fast - slow
        i = fast

    return sum

result = fibonacci(4000000)

print(result)
'''