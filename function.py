#function:add_numbers
def add_numbers(num1, num2):
    """Adds two numbers and returns their sum."""
    return num1 + num2

#function:is_even
def is_even(number):
    """Checks if a number is even and returns True or False."""
    return number % 2 == 0
#function:reverse-string
def reverse_string(text):
    """Reverses a string and returns the reversed version."""
    return text[::-1]  # Slicing with a step of -1 reverses the string

#function:count_vowels
def count_vowels(text):
    """Counts the number of vowels in a string and returns the count."""
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count

#function:calculate_factorials
def calculate_factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)
    
#function:apply_decorator
def apply_decorator(func):
    """Applies a decorator to a function."""
    return func
#oop
class Car:
    """Represents a car with make, model, and year."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Prints the car's information."""
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
#sequences
#sort list of tuples
def sort_by_second(tuples):
    return sorted(tuples, key=lambda x: x[1])

#merge dictionaries
#set and dictionary

def merge_dictionaries(dict1, dict2):
    """Merges two dictionaries and returns the merged dictionary."""
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict