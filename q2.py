import random

# Make a random pet.

# Choose:
# Type of animal (at least 3 choices, string)
animal = (["dog", "cat", "fish"])
# Age (integer)
age = random.randint(1,15)
# Color (at least 3 choices, string)
color = (["red", "blue", "golden", "white", "orange", "black", "green"])
# Weight (float)
weight = (["small", "average sized", "large", "fat", "skinny"])

# Print a summary of your pet using an f-string
print(f"Your pet is a {age} year old {random.choices(color)}, {random.choices(weight)}, {random.choices(animal)}")#REPLACE THIS WITH YOUR CODE