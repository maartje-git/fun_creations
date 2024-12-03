"""
https://adventofcode.com/2022/day/12

The heightmap shows the local area from above broken into a grid; the elevation 
of each square of the grid is given by a single lowercase letter, where a is 
the lowest elevation, b is the next-lowest, and so on up to the highest 
elevation, z.

Also included on the heightmap are marks for your current position (S) and the 
location that should get the best signal (E). Your current position (S) has 
elevation a, and the location that should get the best signal (E) has elevation 
z.

You'd like to reach E, but to save energy, you should do it in as few steps as 
possible. During each step, you can move exactly one square up, down, left, or 
right. To avoid needing to get out your climbing gear, the elevation of the 
destination square can be at most one higher than the elevation of your current 
square. This also means that the elevation of the destination square can be 
much lower than the elevation of your current square.
"""

import pathfinder


# Read the file and make a list of all height rows
height_rows = []
with open('221212_trial.txt') as file:
    #  append rows to list
    for line in file:
        height_rows.append(line.strip())


# find the coordinates of S
for i, row in enumerate(height_rows):
    if 'S' in row:
        S_Y = i
        for j, height in enumerate(row):
            if height == 'S':
                S_X = j
                row = row.replace('S', 'a')
                height_rows[i] = row

# find the coordinates of E
for i, row in enumerate(height_rows):
    if 'E' in row:
        E_Y = i
        for j, height in enumerate(row):
            if height == 'E':
                E_X = j
                row = row.replace('E', 'z')
                height_rows[i] = row


# dict for translating letters to numbers
height_values = {}
for i, letter in enumerate(['a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z']):
    height_values[letter] = i

# Make an empty list to apend a matrix to
matrix = [[]*len(height_rows)]
# define height values per letter and put in matrix
for i, row in enumerate(height_rows):
    for j, letter in enumerate(row):
        if letter != 'S' or letter != 'E':
            number = height_values[letter]
            matrix[i].append(number)

        
