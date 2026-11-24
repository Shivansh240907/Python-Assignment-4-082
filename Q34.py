def count_case(text):
    upper = 0
    lower = 0
    for char in text:
        if char.isupper():
            upper = upper + 1
        elif char.islower():
            lower = lower + 1
    return upper, lower

u, l = count_case("Hello Python")
print("Uppercase letters:", u)
print("Lowercase letters:", l)
