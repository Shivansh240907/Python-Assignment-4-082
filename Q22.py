def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print("Largest element:", largest)

my_list = [12, 45, 7, 89, 23]
find_largest(my_list)
