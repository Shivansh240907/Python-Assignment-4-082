def check_prime(num):
    if num <= 1:
        print(num, "is not a prime number")
        return
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            return
    print(num, "is a prime number")

check_prime(11)
check_prime(15)
