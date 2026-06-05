# We can simply go through all unique pairs of three-digit numbers being multiplied together (using the commutativity rule of multiplication)
# Basically, since a x b = b x a we only need to check half of the total combinations

largest = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        p = i * j
        if p > largest and str(p) == str(p)[::-1]:
            largest = p

print(largest)