# -*- coding: utf-8 -*-
"""
Advent of Code 2024
"""

#%% Day 1
"""
Part 1 
Pair up the numbers and measure how far apart they are. Pair up the smallest 
number in the left list with the smallest number in the right list, then the 
second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to 
add up all of those distances.
"""
#Make 2 empty lists
list_1 = []
list_2 = []
#Make variable to count up distances
sum_distances = 0

#Open data and loop through lines.
with open('data_day1.txt') as data:
    for line in data:
        #split line in 2 separate numbers
        number_1, number_2 = line.split('   ',1)
        #append numbers to their appropriate list
        list_1.append(int(number_1))
        list_2.append(int(number_2))

#Sort lists in numerical order
list_1.sort()
list_2.sort()

#Pair numbers from both lists
for number_1, number_2 in zip(list_1,list_2):
    #Check distance
    distance = abs(number_1 - number_2)
    #Add to total distances
    sum_distances += distance
    
"""
Part 2
Calculate a total similarity score by adding up each number in the left list 
after multiplying it by the number of times that number appears in the right list.
"""
#Make variable to count similarity scores
sum_similarity_scores = 0
#Loop through left list
for number in list_1:
    #Check how many times number is in right list and multiply by the number
    similarity_score = number * list_2.count(number)
    #Add to total similarity score
    sum_similarity_scores += similarity_score
    
#%% Day 2
"""

"""
