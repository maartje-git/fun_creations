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
        for i, height in enumerate(row):
            if height == 'S':
                S_X = i

# find the coordinates of E
for i, row in enumerate(height_rows):
    if 'E' in row:
        E_Y = i
        for i, height in enumerate(row):
            if height == 'E':
                E_X = i
    
# define current location:
current_Y = S_Y
current_X = S_X

# define height values per letter
height_values = {}
for i, letter in enumerate(['a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z']):
    height_values[letter] = i

# Get a list with number of steps per trial
number_of_steps = []

#%% Part 1 What is the fewest steps required to move from your current position 
# to the location that should get the best signal?

# Until you are at E check where you can go:
# while current_X != E_X and current_Y != E_Y:
    
#Check current height
current_height_row = height_rows[current_Y]
current_height = current_height_row[current_X]
if current_height == 'S':
    current_height = 'a'

#Check the height on all 4 sides of the current location, compare to current_height
if current_Y > 1:
    height_up_row = height_rows[current_Y - 1]
    height_up = height_up_row[current_X]
    if height_values[height_up] < height_values[current_height] + 2:
        up = True
    else:
        up = False
else:
    up = False

try:
    height_down_row = height_rows[current_Y + 1]
    height_down = height_down_row[current_X]
    if height_values[height_down]  < height_values[current_height] + 2:
        down = True
    else:
        down = False
except:
    down = False
if current_X > 1:
    height_left = current_height_row[current_X - 1]
    if height_values[height_left] < height_values[current_height] + 2:
        left = True
    else:
        left = False
else:
    left = False

try:
    height_right = current_height_row[current_X + 1]
    if height_values[height_right] < height_values[current_height] + 2:
        right = True
    else:
        right = False
except: 
    right = False
    
    



