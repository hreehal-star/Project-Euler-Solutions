# Basically we can take the smaller example of (a + b + c + d)^2
# The expansion results in a^2 + b^2 + c^2 + d^2 + 2(ab + ac + ad + bc + bd + cd)

# We do not need to calculate the sum of individual squares and the square of the sum and then take the difference
# Instead, we can just calculate the difference using the 2(ab + ac + ...) portion of the expansion formula with exponent 2

def square_difference(limit: int):
    difference = 0
    for i in range (1, limit + 1):
        for j in range (i + 1, limit + 1):
            difference += i * j
    return difference * 2

result = square_difference(100)

print(result)