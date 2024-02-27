# Accept user input to create two sets of integers
set1 = set(input("Enter integers for set 1 separated by spaces: ").split())
set2 = set(input("Enter integers for set 2 separated by spaces: ").split())

# Create a new set containing only the common elements from both sets
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)
