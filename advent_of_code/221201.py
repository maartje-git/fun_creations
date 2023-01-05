"""
https://adventofcode.com/2022/day/1
"""
# Find the Elf carrying the most Calories. 
# How many total Calories is that Elf carrying?
with open('221201.txt') as file:

    # Start out with 0 calories
    calories = 0
    
    # make an empty list to append calories to
    calorie_list = []
    
    # Loop through the lines in the data
    for line in file:
        # Remove all line breaks
        line = line.replace('\n', '')
        # If after removing line break, the string is not empty
        # Add the calories in that line to the sum
        if line != '':
            calories = calories + int(line)
        # If after removing line breaks, the string is empty
        # append the current sum of calories the calorie_list 
        # Reset the calories counter
        else:
            calorie_list.append(calories)
            calories = 0

# print the highest calories sum
print(max(calorie_list))

# Find the top three Elves carrying the most Calories. 
# How many Calories are those Elves carrying in total?

# Reverse sort the calories_list and show get only the top_3
top_3 = sorted(calorie_list, reverse=True)[:3]
# Calculate the total calories for the top 3
print(sum(top_3))
