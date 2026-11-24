def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

my_list = [12, 45, 7, 89, 23]
result = find_largest(my_list)
print("Largest element:", result)
