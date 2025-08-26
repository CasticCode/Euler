current = 3
sum = 2
prev = 2

while current <= 4000000:
    temp = current
    current = current + prev
    prev = temp
    if current % 2 == 0:
        sum += current
print(sum)