# Accept user input to create a list of integers
numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Compute the sum of all the integers in the list
sum_of_numbers = sum(numbers)
print("Sum of the integers:", sum_of_numbers)
