# We just need to use modulus division to check if each number in the sequence is divisible by 3 or 5
# If the number is divisible by 3 or 5 then we add it to the sum


def calculate_sum(upper_bound: int):
    sum = 0
    for i in range (0, upper_bound):
        if i % 5 == 0 or i % 3 == 0:
         sum += i
    return sum

result = calculate_sum(1000)
print(result)