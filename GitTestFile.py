sum = 0
for number in range(1, 1000):
    number = list(str(number))
    for digit in number:
        digit = int(digit)
        sum = sum + digit

print(sum)
print(sum + 1)
print(sum + 2)