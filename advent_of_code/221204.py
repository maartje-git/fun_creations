"""
https://adventofcode.com/2022/day/4

Elves have been assigned the job of cleaning up sections of the camp.
They've noticed that many of the assignments overlap.
Elves pair up and make a big list of the section assignments for each pair.
Some of the pairs have noticed that one of their assignments fully contains 
the other. For example, 2-8 fully contains 3-7, 
and 6-6 is fully contained by 4-6.
"""

# In how many assignment pairs does one range fully contain the other?

import pandas as pd

df = pd.DataFrame()

with open('221204.txt') as file:
    # Loop through lines of the data
    for line in file:
        # Split data in 2 seperate assignments
        assignment_1 , assignment_2 = line.split(',')[0], line.split(',')[1] 
        
        # Make 2 empty lists to write out all sections per assignment
        sections_1 = []
        sections_2 = []
        
        # loop through sections and append them to sections lists
        for i in range(
                int(assignment_1.split('-')[0]), 
                int(assignment_1.split('-')[1])+1):
            sections_1.append(i)
        for i in range(
                int(assignment_2.split('-')[0]), 
                int(assignment_2.split('-')[1])+1):
            sections_2.append(i)
        
        # Make a set object from sections_1 to be able to find overlap
        sections_1_set = set(sections_1)
        # check where sections_1 and sections_2 overlap
        overlap = sorted(list(sections_1_set.intersection(sections_2)))
        
        # check whether one of the assignments is completely
        # inside the other assignment
        if overlap == sections_1 or overlap == sections_2:
            fully_overlap = True
        else:
            fully_overlap = False
    
        # Make a dict of all new info ;per line of the file
        new_row = {
            'assignment_1': assignment_1, 
              'assignment_2': assignment_2, 
              'sections_1': sections_1, 
              'sections_2':  sections_2,
              'overlap': overlap,
              'fully_overlap': fully_overlap} 
        
        # Append the infocfor every line to the df 
        df = df.append(new_row, ignore_index=True)

# Count for how many pairs there is a full overlap        
fully_overlap_count_1 = df.fully_overlap.value_counts()

# Instead, the Elves would like to know the number of pairs that overlap at all.
# In how many assignment pairs do the ranges overlap?

# Loop through df
for i in df.index:
    # For every pair extract the overlapping sections
    overlap = df['overlap'][i]
    
    # Count how many sections overlap, and check whether there is at least 1
    if len(overlap) > 0:
        any_overlap = True
    else:
        any_overlap = False
    
    # Add a new colum to the df, with info whether there is at least 1 overlap
    df.at[i,'any_overlap'] = any_overlap

# Count for how many pairs there is at least 1 section overlapping
any_overlap_count = df.any_overlap.value_counts()



            
                
            
        
               
        
        