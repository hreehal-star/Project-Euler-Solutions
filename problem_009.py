# We can simply loop through the combinations of a and b and take the case where b > a
# Then we can manipulate the equation of a + b + c = 1000 to check if the Pythagorean triple holds true

def find_triple(target:int ):
    for a in range(1, target):
        for b in range(a + 1, target):
            c = target - a - b

            if a*a + b*b == c*c:
                triple = [a, b, c]
                break
    return triple

result = find_triple(1000)
print(result)

# Calculating the product a*b*c
product = 1
for i in range(0, 3):
    product *= result[i]

print(product)