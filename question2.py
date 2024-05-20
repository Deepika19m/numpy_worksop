# find if the given number is a palindrome or not?


#solution

def is_palindrome(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        return True
    else:
        return False
try:
    number = int(input("Enter a number: "))
    if is_palindrome(number):
        print(f"The number {number} is a palindrome.")
    else:
        print(f"The number {number} is not a palindrome.")
except ValueError:
    print("Please enter a valid integer.")

