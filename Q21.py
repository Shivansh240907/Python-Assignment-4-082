def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10
    print("Sum of digits:", total)

sum_of_digits(1234)
