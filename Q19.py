def check_palindrome(text):
    if text == text[::-1]:
        print(text, "is a palindrome")
    else:
        print(text, "is not a palindrome")

check_palindrome("madam")
check_palindrome("hello")
