def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")  # Output: The average is: 0

my_numbers = [10, 20, 30]
result = calculate_average(my_numbers)
print(f"The average is: {result}")  # Output: The average is: 20.0

my_numbers = [10, 20, 30, 0]
result = calculate_average(my_numbers)
print(f"The average is: {result}") # Output: The average is: 15.0