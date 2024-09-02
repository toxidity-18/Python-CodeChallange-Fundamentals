def add_numbers(num1, num2):
    """Adds two numbers."""
    return num1 + num2
print(add_numbers(3.5, 2.7)) 


def is_even(number: int) -> bool:
    """Checks if a number is even."""
    return number % 2 == 0
print(is_even(10)) 
print(is_even(11))

def reverse_string(text):
    """Reverses a string."""
    return text[::-1]
print(reverse_string("abcdefg"))

def count_vowels(text):
    """Counts vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
print(count_vowels("Samuel"))



def calculate_factorial(n):
    """Calculates the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)
    result = calculate_factorial(5)
    print(f"The factorial of 5 is {result}")
    
    
def apply_decorator(func):
    """Applies a decorator to a function."""
    def wrapper():
        print("Decorator Applied")
        return func()
        return wrapper

