digits = input()

sum = 0
for i in range(len(digits)):
    if digits[i] == digits[(i + len(digits) // 2) % len(digits)]:
        sum += int(digits[i])

print(sum)
