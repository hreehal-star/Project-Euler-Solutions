# The fundamental theorem of arithmetic says that all integers can be broken down into a product of prime numbers
# By using this fact, we can immediately multiply all prime numbers from 1 to 20
# Then, every other factor can be accounted for by multiplying our number by either 2, 3, or both (6)
# Once the number can be divided evenly by all integers from 1 to 20, we can simply return it

def lowestDividend(limit: int):
    num = 1*2*3*5*7*11*13*17*19

    i = 1
    while(i <= limit):
        if num % i == 0:
            i += 1
        else:
            if (i % 6 == 0):
                num = num * 6
            elif(i % 3 == 0):
                num = num * 3
            else:
                num = num * 2
            i = 1
    return num

result = lowestDividend(20)
print(result)
