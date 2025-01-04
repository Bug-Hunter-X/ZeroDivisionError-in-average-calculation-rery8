def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Alternative solution using try-except block:
def calculate_average_try_except(numbers):
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except ZeroDivisionError:
        return 0 #or handle it in a more appropriate way for your use case

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average_try_except(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average_try_except(my_empty_list)
print(f"The average of an empty list is: {average_empty}") 