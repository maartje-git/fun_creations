# -*- coding: utf-8 -*-
"""
Advent of Code 2024
"""

#%% Day 1
"""
Pair up the numbers and measure how far apart they are. Pair up the smallest 
number in the left list with the smallest number in the right list, then the 
second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to 
add up all of those distances.
"""
#make 2 empty lists
list_1 = []
list_2 = []

#open data and loop through lines.
with open('advent_of_code/2024/data_day1.txt') as data:
    for line in data:
        #split line in 2 separate numbers
        number_1, number_2 = line.split('   ‘,1)
        #append numbers to their appropriate list
        list_1.append(int(number_1))
        list_2.append(int(number_2))




