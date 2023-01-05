"""
https://adventofcode.com/2022/day/3

A given rucksack always has the same number of items in each of its two 
compartments, so the first half of the characters represent items in the first 
compartment, while the second half of the characters represent items in the 
second compartment.

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
"""
# Find the item type that appears in both compartments of each rucksack. 
# What is the sum of the priorities of those item types?

import pandas as pd
df = pd.DataFrame()

with open('221203.txt') as file:
    # Loop through the lines of the file
    for line in file:
        # Divide the line exactly in 2
        comp1, comp2 = line[:len(line)//2], line[len(line)//2:]
        # Loop through the items in the first halve
        for x in comp1:
            # Check if they match any of the items in the second halve
            for y in comp2:
                if x == y:
                    # if they match, assign the item to the match variable
                    match = x
                    # check whether it is upper or lower case
                    # And assign it's priority accordingly
                    if x.isupper():
                        priority = ord(x) - 38
                    else:
                        priority = ord(x) - 96

        # Collect all new info for each line in the file
        new_row = {
            'line': line.strip(),
            'comp1': comp1, 
            'comp2': comp2, 
            'double_item': match, 
            'priority': priority} 
        
        # For each line in the file, append the new info to the df
        df = df.append(new_row, ignore_index=True)

# Calculate the sum of priorities
priority_sum = df['priority'].sum()

# Every set of three lines in your list corresponds to a single group
# Find the one item type that is common between all three Elves in each group.
#  What is the sum of the priorities of those item types?

# Loop through the df
for index, row in df.iterrows():
    # Group every 3 lines together
    index3 = index + 1
    if index3%3 == 0:
        # At every 3rd line, loop through items
        for x in df['line'][index -2]:
            # Check if any of them match any items of the line above
            for y in df['line'][index -1]:
                if x == y:
                    # If any items match, also check if they match any item in
                    # the line above that one
                    for z in df['line'][index]:
                        if x == z:
                            # IF there is a match between all 3 lines, assign
                            # that item to the badge variable
                            badge = x
                            
                            # check whether it is upper or lower case
                            # And assign it's priority accordingly 
                            if x.isupper():
                                priority = ord(x) - 38
                            else:
                                priority = ord(x) - 96
                            
                            # Append the new info (badge item and priority)
                            # to the df
                            df.at[index,'badge'] = badge
                            df.at[index,'badge_priority'] = priority

# Calculate the sum of priorities
badge_priority_sum = df['badge_priority'].sum()
        
