#list prime factors of inputted number

def findFactor(num):
    factors = []
    factor = 2
    while num >=2:
        if num % factor == 0:
            factors.append(factor)
            num = num // factor
        else:
            factor+=1
    factors = list(set(factors))
    return factors

print(findFactor(int(input("Number to be prime factored"))))