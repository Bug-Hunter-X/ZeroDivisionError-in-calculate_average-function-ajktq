def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# This is buggy
my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}") #this will give an error if the list is empty

my_numbers = [10, 20, 30]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = [10, 20, 30, 0]
result = calculate_average(my_numbers)
print(f"The average is: {result}")