def add_numbers(*args):
    total = sum(args)
    print("Numbers:", args)
    print("Sum:", total)

add_numbers(10, 20)
add_numbers(5, 10, 15, 20)
