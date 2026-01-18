# -*- coding: utf-8 -*-
"""
Advent of Code 2024
"""

#%% Day 1
"""
Part 1 
There are two lists of numbers. Pair up the numbers and measure how far apart 
they are. Pair up the smallest number in the left list with the smallest number 
in the right list, then the second-smallest left number with the second-
smallest right number, and so on.

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

print(f'Day 1.1: {sum_distances}')
    
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

print(f'Day 1.2: {sum_similarity_scores}')
    
#%% Day 2
"""
your puzzle input consists of many reports, one report per line. Each report is 
a list of numbers called levels that are separated by spaces.
a report only counts as safe if both of the following are true:
- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.
How many reports are safe?
"""
def check_if_in_decreasing(numbers):
    """
    Check if  numbers in list are increasing or decreasing
    """
    if numbers == sorted(numbers) or numbers == sorted(numbers, reverse = True):
        return True 

def check_differences(numbers):
    """
    Check differences between adjecent numbers and check if all
    differences are within 0 < x < 4
    """
    differences = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]
    safe = sum(not (0 < diff < 4) for diff in differences) == 0
    
    return safe

# Part 1
with open('data_day2.txt') as data:
    reports = [list(map(int, report.split())) for report in data]
    # Loop through reports
    counter_1 = 0
    for report in reports:
    # Check if check if they are increasing or decreasing
        if check_if_in_decreasing(report):
            # if True, then check differences
            if check_differences(report):
                counter_1 += 1

# Part 2 Tolerate a single bad level
    counter_2 = 0
    for report in reports:
    # Check if they are increasing or decreasing
        if check_if_in_decreasing(report):
            # if True, then check differences
            if check_differences(report):
                counter_2 += 1
            # Check if differences would be ok if you remove 1 level
            else:
                #Loop through levels and remove them 1 by 1
                for i in range(len(report)):
                    new_report = report[:i] + report[i+1:]
                    if check_differences(new_report):
                        counter_2 += 1
                        break
        # Check if they would be increasing if you remove 1 level            
        else:
            #Loop through levels and remove them 1 by 1
            for i in range(len(report)):
                new_report = report[:i] + report[i+1:]
                # Check if they are increasing or decreasing
                if check_if_in_decreasing(new_report):
                    # if True, then check differences
                    if check_differences(new_report):
                        counter_2 += 1
                        break
print(f'Day_2.1: {counter_1}')
print(f'Day 2.2: {counter_2}')
                
#%% Day 3
"""
The computer appears to be trying to run a program, but its memory (your puzzle 
input) is corrupted. All of the instructions have been jumbled up!
The goal of the program is just to multiply some numbers. It does that with 
instructions like mul(X,Y).
Scan the corrupted memory for uncorrupted mul instructions. What do you get if 
you add up all of the results of the multiplications?
"""
# Part 1
# Parse the memory
data = open('data_day3.txt').read()
multiplication = 0

#split data by mul instruction
split_data = data.split('mul(')

# Loop through instructions
for mul in split_data:
    #Check if following are 1, 2 or 3 digits, followed by ,
    try:
        first_digit, second_part = mul.split(',', 1)
    except:
        pass
    #Check if second part is a 1, 2 or 3 digits number, followed by )
    try:
        second_digit = second_part.split(')',1)[0]
    except:
        pass
    #If both are digits, parse them to dict
    if first_digit.isdigit() and second_digit.isdigit():
        multiplication += (int(first_digit)*int(second_digit))
    first_digit = ''
    second_digit = ''
print(multiplication)

# Part 2        
"""
There are two new instructions you'll need to handle:
- The do() instruction enables future mul instructions.
- The don't() instruction disables future mul instructions.
"""
# Parse the memory
data = open('data_day3.txt').read()
multiplication_2 = 0

# Split data by do instruction
do_dont = data.split('do(')
do_data = []
dont_data = []
# Split data by don't instruction
for data in do_dont:
    try:
        do , dont = data.split("don't(",1)
        do_data.append(do)
        dont_data.append(dont)
    # Also if there is no don't, it needs to be added to do_data
    except:
        do_data.append(data)

# Loop through the do parts
for do in do_data:
    #split data by mul instruction
    split_data = do.split('mul(')

    # Loop through instructions
    for mul in split_data:
        #Check if following are 1, 2 or 3 digits, followed by ,
        try:
            first_digit, second_part = mul.split(',', 1)
        except:
            pass
        #Check if second part is a 1, 2 or 3 digits number, followed by )
        try:
            second_digit = second_part.split(')',1)[0]
        except:
            pass
        #If both are digits, parse them to dict
        if first_digit.isdigit() and second_digit.isdigit():
            multiplication_2 += (int(first_digit)*int(second_digit))
        first_digit = ''
        second_digit = ''


print(multiplication_2)

#%% Day 4
"""
Help with word search (your puzzle input). She only has to find one word: XMAS
Horizontal, vertical, diagonal, backwards, or overlapping other words.
How many times does XMAS appear?
"""
# Parse the memory
lines = []
with open('data_day4.txt') as data:
    for line in data: # Read lines as strings
        lines.append(line.strip())

# Start a counter
XMAS_count = 0

# Search directions as (row_step, col_step)
directions = [
    (-1, -1),  # NW
    (-1, 0),   # N
    (-1, 1),   # NE
    (0, -1),   # W
    (0, 1),    # E
    (1, -1),   # SW
    (1, 0),    # S
    (1, 1),    # SE
]

# Dimensions of the grid
number_of_lines = len(lines)
number_of_letters = len(lines[0])

# Function to check if "XMAS" exists in a given direction
def check_word(line, letter, line_step, letter_step):
    for offset, char in enumerate("XMAS"):
        line_to_check = line + line_step * offset
        letter_to_check = letter + letter_step * offset
        # Explicit bounds check to avoid negative indexing or overflow
        if line_to_check < 0 or line_to_check >= number_of_lines or letter_to_check < 0 or letter_to_check >= number_of_letters:
            return False
        if lines[line_to_check][letter_to_check] != char:
            return False
    return True

# Iterate through the grid
for line in range(number_of_lines):
    for letter in range(number_of_letters):
        if lines[line][letter] == 'X':  # Start checking if the letter is 'X'
            for line_step, letter_step in directions:
                if check_word(line, letter, line_step, letter_step):
                    XMAS_count += 1

print(f'XMAS count = {XMAS_count}')
#%% Day 4, Part 2
"""
It's an X-MAS puzzle in which you're supposed to find two MAS in the shape of 
an X.

M.S
.A.
M.S
"""            
# Parse the memory
lines = []
with open('data_day4.txt') as data:
    for line in data: # Read lines as strings
        lines.append(line.strip())

# Dimensions of the grid
number_of_lines = len(lines)
number_of_letters = len(lines[0])

XMAS_count_2 = 0

# Function to check if "MAS" exists in any direction in the X shape
def check_X(line, letter):
    # Ensure that the "X" pattern fits within the grid boundaries
    if (line - 1 < 0 or line + 1 >= number_of_lines or 
        letter - 1 < 0 or letter + 1 >= number_of_letters):
        return False
    
    # Check if the surrounding letters form a valid "X"-shaped MAS pattern
    nw_se = lines[line - 1][letter - 1] + lines[line + 1][letter + 1]  
    ne_sw = lines[line - 1][letter + 1] + lines[line + 1][letter - 1]
    if sorted(nw_se) == ['M','S'] and sorted(ne_sw) == ['M','S']:  # Ensure 2 M's and 2 S's
        return True

# Iterate through the grid
for line in range(number_of_lines):
    for letter in range(number_of_letters):
        if not line - 1 < 0 or line + 1 >= number_of_lines or letter - 1 < 0 or letter + 1 >= number_of_letters:
            if lines[line][letter] == 'A':  # Start checking if the letter is 'A'
                if check_X(line, letter):
                    XMAS_count_2 += 1

                         
print(f'X-MAS count = {XMAS_count_2}')

#%% Day 5
"""
Determine which updates are already in the correct order. What do you get if 
you add up the middle page number from those correctly-ordered updates?
"""
import math
rules = {}
updates = []


with open('fun_creations/advent_of_code/2024/data_day5.txt') as data:
    for line in data: # Read lines as strings
        if '|' in line:
            first_page, second_page = line.split('|')
            first_page = int(first_page)
            second_page = int(second_page)
            
            if first_page not in rules.keys():
                rules[first_page] = [second_page]
            else:
                rules[first_page].append(second_page)

        elif ',' in line:
            pages = []
            for page in line.split(','):
                page = page.strip() # Remove \n after last page
                pages.append(int(page))
            updates.append(pages)

counter = 0             
for update in updates:
    status = True
    check = {}
    for i, page in enumerate(update):
        # Check if page is a key in rules
        if page in rules.keys():
            before_pages = rules[page] 
            # Loop through pages 
            for page_to_check in update[:i]:
                # Check if they are in the rules of the current page
                if page_to_check in before_pages:
                    status = False
                    break
    
    if status == True:    
        middle_page = update[math.ceil(len(update)/2 ) -1]
        counter += middle_page

print(f'Day5.1: {counter}')

"""
Find the updates which are not in the correct order. What do you get if you 
add up the middle page numbers after correctly ordering just those updates?
"""
counter2 = 0            
for update in updates:
    status = True
    check = {}
    for loop in range(len(update)):
        for i, page in enumerate(update):        
            # Check if page is a key in rules
            if page in rules.keys():
                before_pages = rules[page] 
                # Loop through pages 
                for p_i, page_to_check in enumerate(update[:i]):
                    # Check if they are in the rules of the current page
                    if page_to_check in before_pages:
                        status = False                    
                        update.insert(i, update.pop(p_i))
                        break

    if status == False:
        
        middle_page = update[math.ceil(len(update)/2 ) -1]
        counter2 += middle_page
        
print(f'Day5.2: {counter2}')

#%% Day 6
"""
a map (your puzzle input) of the situation.
Guard < ^ > v indicates direction she is facing
# obstructions
Guard move rules:
    - If there is something directly in front of you, turn right 90 degrees.
    - Otherwise, take a step forward.
    - leaves the mapped area when walking past an obstruction out of the map
    
How many distinct positions will the guard visit before leaving the mapped area?
"""
# Get the map in lists inside list format and find the guard in the map
map_grid = []
with open('fun_creations/advent_of_code/2024/data_day6.txt') as data:
    for i, line in enumerate(data):
        line_list = []
        for character in line.strip():
            line_list.append(character)
        map_grid.append(line_list)
        if '^' in line:
            starting_line = i
            for i, spot in enumerate(line):
                if spot == '^':
                    starting_spot = i

# Get map boundaries
map_width, map_height = (len(map_grid[0]), len(map_grid))
# GEt guard starting position
guard_position = (starting_line, starting_spot)

# Def for finding the next position of the guard, based on the orientation of the guard
def get_next_position(current_pos, orientation):
    """Calculate next position based on orientation."""
    row, col = current_pos
    moves = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }
    delta_row, delta_col = moves[orientation]
    return (row + delta_row, col + delta_col)

# If guard faces an obstacle, she turns clockwise
def get_next_direction(current_direction):
    """Get next direction when rotation is needed."""
    rotation = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return rotation[current_direction]

# Make a list to append all locations the guard will visit to
guard_positions = [guard_position]

# Let the guard walk around
while True:
    # Check the guards orientation
    guard_orientation = map_grid[guard_position[0]][guard_position[1]]
    # Get the next position the guard would walk to
    next_position = get_next_position((guard_position[0],guard_position[1]), guard_orientation)
    
    # Check if next position is out of bounds of the map
    if next_position[0] < 0 or next_position[0] > map_width - 1 or next_position[1] < 0 or next_position[1] > map_height - 1:
        # If the guard walks out of the map, the task is done
        break
    else:
        # If the guard is not walking out of the map, check if there is an obstacle
        if map_grid[next_position[0]][next_position[1]] == '#':
            # If there is an obstacle, change direction
            next_orientation = get_next_direction(guard_orientation)
            map_grid[guard_position[0]][guard_position[1]] = next_orientation
        else:
            # If there is no obstacle, walk in current direction
            map_grid[guard_position[0]][guard_position[1]] = '.'                
            guard_position = next_position
            map_grid[guard_position[0]][guard_position[1]] = guard_orientation 
            # Add the new position to the list with all visited loacations
            guard_positions.append(guard_position)

# Filter out any double visited positions                      
distinct_guard_positions = list(dict.fromkeys(guard_positions))
print(f'Day6.1: {len(distinct_guard_positions)}') 
 
# Day 6.2
"""
You need to get the guard stuck in a loop by adding a single new obstruction. 
How many different positions could you choose for this obstruction?
"""
# Make a list to append obstacles to that cause an infinite loop
infinite_loop_positions = []
# If the guard is on an already visited position, in the same orenitation, the guard is stuck in a loop
# So make a set, for position/orientation combinations
position_direction_history = set()
# Add the starting position/orientation
position_direction_history.add((guard_position,'^'))

# Loop through all positions the guard will visit
for i, j in distinct_guard_positions:
    # Reset guard and map for every new obstacle
    guard_position = (starting_line, starting_spot)
    map_grid[guard_position[0]][guard_position[1]] = '.'        
    guard_positions = [guard_position]
    position_direction_history = set()
    position_direction_history.add((guard_position,'^'))
    map_grid[guard_position[0]][guard_position[1]] = '^'

    # You cannot place an opbstacle on the starting position of the guard
    if not (i,j) == guard_position:
 
        # Place obstacle
        map_grid[i][j] = '#'
        
        # Let the guard walk around
        while True:
            # Check the guards orientation
            guard_orientation = map_grid[guard_position[0]][guard_position[1]]
            # Get the next position the guard would walk to
            next_position = get_next_position((guard_position[0],guard_position[1]), guard_orientation)
            
            # Check if next position is out of bounds of the map
            if next_position[0] < 0 or next_position[0] > map_width - 1 or next_position[1] < 0 or next_position[1] > map_height - 1:
                # If the guard walks out of the map, the task is done
                break
            else:
                # If the guard is not walking out of the map, check if there is an obstacle
                if map_grid[next_position[0]][next_position[1]] == '#':
                    # If there is an obstacle, change direction
                    next_orientation = get_next_direction(guard_orientation)
                    map_grid[guard_position[0]][guard_position[1]] = next_orientation
                else:
                    # If there is no obstacle, walk in current direction
                    map_grid[guard_position[0]][guard_position[1]] = '.'                
                    guard_position = next_position
                    map_grid[guard_position[0]][guard_position[1]] = guard_orientation 
                    # Add the new position to the list with all visited loacations
                    guard_positions.append(guard_position)
                    
                    # Check if the guard has been in the this position in the same orientation before
                    if (guard_position,guard_orientation) in position_direction_history:
                        # If yes, then the guard is stuck
                        infinite_loop_positions.append((i,j))
                        break
                    else:
                        position_direction_history.add((guard_position,guard_orientation))

        # Remove the obstacle that was placed
        map_grid[i][j] = '.'
        
print(f'Day6.2: {len(infinite_loop_positions)}')        

#%% Day 7
"""
determine whether the numbers can be combined with operators to produce the 
test value. Only + and * operators are possible.
Operators are always evaluated left-to-right, not according to precedence rules.
Determine which equations could possibly be true. What is their total calibration result?
"""
import itertools

# Get the data and make a list with equations
equations = []
with open('fun_creations/advent_of_code/2024/data_day7.txt') as data:
    # Read lines as strings
    for line in data: 
        # Split string in test_value and remaining numbers
        test_value, values = line.split(': ') 
        # Separate the remaining numbers, strip from new line, spaces etc, and make into int
        numbers = []
        for number in values.split(' '):
            number.strip()
            numbers.append(int(number))
        # Make a dict with the test_value as key, and the list with remanining numbers as value
        equation = {int(test_value): numbers}
        # Append to the list with all the equations
        equations.append(equation)

# Get a variable for adding up all the test_values that are true
total_calibration_result = 0


# Loop through the equations
for equation in equations:
    # There is only one, but loop gets the test_value out
    for test_value in equation.keys():
        # Get the remaining numbers for that test_value
        numbers = equation[test_value]
        
        # Possible operator combinations
        operator_combinations = itertools.product(['+', '*'], repeat=len(numbers)-1)
        
        # Set to track already counted test values for this equation, to avoid double counts
        counted_test_values = set()
        
        # Make all possible expressions with all possible operator combinations
        for operators in operator_combinations:
            expression = str(numbers[0])  # Start with the first number
            for i, operator in enumerate(operators):
                expression += f" {operator} {numbers[i + 1]}"

                # Check if similar to test_value
                # Split the expression into numbers and operators
                tokens = expression.split()
                # Start with the first number as the initial result
                result = int(tokens[0])
                # Iterate over the operators and numbers
                for i in range(1, len(tokens), 2):
                    operator = tokens[i]
                    number = int(tokens[i + 1])
    
                    # Apply the operator to the current result
                    if operator == '+':
                        result += number
                    elif operator == '*':
                        result *= number
                
                
                # If the result matches the test_value and it hasn't been counted already
                if result == test_value and test_value not in counted_test_values:
                    total_calibration_result += test_value
                    counted_test_values.add(test_value)  # Mark this test_value as counted for this equation
                    break  # We can stop checking further combinations for this test_value
                
print(f'Day7.1: {total_calibration_result}')           
#%% Day 7.2     
"""
Third operator: ||

"""
import itertools

# Get the data and make a list with equations
equations = []
with open('fun_creations/advent_of_code/2024/data_day7.txt') as data:
    for line in data:
        test_value, values = line.split(': ') 
        numbers = [int(x.strip()) for x in values.split()]
        equations.append((int(test_value), numbers))

# Get a variable for adding up all the test_values that are true
total_calibration_result = 0

# Loop through the equations
for test_value, numbers in equations:
    # Possible operator combinations
    operator_combinations = itertools.product(['+', '*','||'], repeat=len(numbers)-1)
    
    # Set to track already counted test values for this equation, to avoid double counts
    counted_test_values = set()
    
    # Make all possible expressions with all possible operator combinations
    for operators in operator_combinations:
        expression = str(numbers[0])  # Start with the first number
        for i, operator in enumerate(operators):
            expression += f" {operator} {numbers[i + 1]}"

        # Check if similar to test_value
        # Split the expression into numbers and operators
        tokens = expression.split()
        # Start with the first number as the initial result
        result = int(tokens[0])
        # Iterate over the operators and numbers

        for i in range(1, len(tokens), 2):
            operator = tokens[i]
            number = int(tokens[i + 1])

            # Apply the operator to the current result
            if operator == '||':
                new_number = str(result) + tokens[i + 1]
                result = int(new_number)

            elif operator == '+':
                result += number
            elif operator == '*':
                result *= number
 
        # If the result matches the test_value and it hasn't been counted already
        if result == test_value and test_value not in counted_test_values:
            total_calibration_result += test_value
            counted_test_values.add(test_value)  # Mark this test_value as counted for this equation
            break  # We can stop checking further combinations for this test_value
print(f'Day7.2: {total_calibration_result}')

#%% Day 7.2 faster
import itertools

def evaluate_expression(numbers, operators):
    """
    Evaluate an expression based on the numbers and operators list.
    """
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i - 1] == '+':
            result += numbers[i]
        elif operators[i - 1] == '*':
            result *= numbers[i]
        elif operators[i - 1] == '||':
            result = int(str(result) + str(numbers[i]))
    return result

# Get the data and make a list with equations
equations = []
with open('fun_creations/advent_of_code/2024/data_day7.txt') as data:
    for line in data:
        test_value, values = line.split(': ') 
        numbers = [int(x.strip()) for x in values.split()]
        equations.append((int(test_value), numbers))

# Initialize the total calibration result
total_calibration_result = 0

# Loop through the equations
for test_value, numbers in equations:
    # Possible operator combinations (excluding || for single numbers)
    operator_combinations = itertools.product(['+', '*', '||'], repeat=len(numbers)-1) if len(numbers) > 1 else [()]

    # Track if we've already counted a valid result for the current test_value
    counted_test_values = set()

    # Check all possible combinations of operators
    for operators in operator_combinations:
        # Ensure we don't repeat the same combination of operators for the same test_value
        if test_value not in counted_test_values:
            result = evaluate_expression(numbers, operators)
            
            if result == test_value:
                total_calibration_result += test_value
                counted_test_values.add(test_value)  # Mark as counted
                break  # No need to check further combinations for this test_value

print(f'Day7.2: {total_calibration_result}')

#%% Day 8
"""
Puzzle input is a map of antennas.
an antinode occurs at any point that is perfectly in line with two antennas of 
the same frequency - but only when one of the antennas is twice as far away as the other.
How many unique locations within the bounds of the map contain an antinode?
"""
# Get the map in lists inside list format
map_grid = []
with open('fun_creations/advent_of_code/2024/data_day8.txt') as data:
    for line in data:
        map_grid.append(list(line.strip()))
        
# Precompute map dimensions
map_width, map_height = len(map_grid[0]), len(map_grid)

def out_of_bounds(position, map_width, map_height):
    """
    Check whether a specific location is on the map, or out of bounds
    """
    return position[0] < 0 or position[0] >= map_width or position[1] < 0 or position[1] >= map_height


def check_other_antennae(map_grid, antenna):
    """
    Check the rest of the grid for similar antennae, and provide their location
    """
    matched_antennae = []

    for i, line in enumerate(map_grid):
        for j, spot in enumerate(line):
            if spot == antenna:
                matched_antennae.append((i,j))
    
    return (matched_antennae)

# # Make a list of antinode locations
# antinode_locations = set()
# # loop through lines of the map
# for l, line in enumerate(map_grid):
#     # Loop through specific spots in each line
#     for s, spot in enumerate(line):
#         # Check for antenna
#         if not spot == '.':
#             # Antenna positions:
#             antenna_position = (l,s)
#             # Check for similar antennae
#             antenna = spot
#             matched_antennae = check_other_antennae(map_grid, antenna)
            
#             # Drop self
#             matched_antennae.remove(antenna_position)
            
#             # Get annode locations
#             for matched_antenna in matched_antennae:
#                     annode_line = antenna_position[0] - (matched_antenna[0] - antenna_position[0])
#                     annode_spot = antenna_position[1] - (matched_antenna[1] - antenna_position[1])
#                     annode_location = (annode_line,annode_spot)
#                     # Check if anode is on the grid
#                     if not out_of_bounds(annode_location, map_width, map_height):
#                         # Add the location to antinode locations
#                         antinode_locations.add(annode_location)
# print(f'Day 8.1: {len(antinode_locations)}')
            
"""
Take effects of resonant harmonics into account.

"""        
# Make a list of antinode locations
antinode_locations = set()
# loop through lines of the map
for l, line in enumerate(map_grid):
    # Loop through specific spots in each line
    for s, spot in enumerate(line):
        # Check for antenna
        if not spot == '.':
            # Antenna positions:
            antenna_position = (l,s)
            
            # Check for similar antennae
            antenna = spot
            matched_antennae = check_other_antennae(map_grid, antenna)
            
            # Drop self
            matched_antennae.remove(antenna_position)
            if len(matched_antennae) > 0 :
                antinode_locations.add(antenna_position)
            
            # Get annode locations
            for matched_antenna in matched_antennae:
                    annode_line = antenna_position[0] - (matched_antenna[0] - antenna_position[0])
                    annode_spot = antenna_position[1] - (matched_antenna[1] - antenna_position[1])
                    annode_location = (annode_line,annode_spot)
                    # Check if anode is on the grid
                    if not out_of_bounds(annode_location, map_width, map_height):
                        # Add the location to antinode locations
                        antinode_locations.add(annode_location)
                    
                    while True:
                        annode_line = annode_line - (matched_antenna[0] - antenna_position[0])
                        annode_spot = annode_spot - (matched_antenna[1] - antenna_position[1])
                        annode_location = (annode_line,annode_spot)
                        # Check if anode is on the grid
                        if not out_of_bounds(annode_location, map_width, map_height):
                            # Add the location to antinode locations
                            antinode_locations.add(annode_location)
                        else:
                            break

print(f'Day 8.2: {len(antinode_locations)}')

#%% Day 9
"""
disk map (your puzzle input)
The digits alternate between indicating the length of a file and the 
length of free space.
Each file on disk also has an ID number.
Move file blocks one at a time from the end of the disk to the leftmost free space block
update the filesystem checksum.
"""
# Get the data
with open('fun_creations/advent_of_code/2024/data_day9t.txt') as data:
    disk_map = data.readline().strip()

# Get the individual file blocks
compact_file = []
file_ID = 0
# Loop through disk_map
for i, digit in enumerate(disk_map):
    size = int(digit)
    if i % 2 == 0:
        # File block: Add `size` instances of the file ID
        compact_file.extend([file_ID] * size)
        file_ID += 1
    else:
        # Free space: Add `size` instances of free space (represented by '.')
        compact_file.extend(['.'] * size)

# Compacting the files
free_spaces = compact_file.count('.')

# While there is still free space
while free_spaces > 0:
    # Loop through files in reversed order
    for i in range(len(compact_file) - 1, -1, -1):
        # If there is a file, move it to the first free space
        if compact_file[i] != '.':
            # Find the leftmost free space
            for j in range(len(compact_file)):
                if compact_file[j] == '.':
                    compact_file[j] = compact_file[i]
                    compact_file[i] = '.'  # Mark the file's original position as free space
                    free_spaces -= 1
                    break

# Calculate the checksum
checksum = sum((i-1) * (int(file) if file != '.' else 0) for i, file in enumerate(compact_file))

print(f'Day 9.1: {checksum}')
    
#%% Day 9.2

# Get the data
with open('fun_creations/advent_of_code/2024/data_day9.txt') as data:
    disk_map = data.readline().strip()

# Get the individual file blocks
compact_file = []
file_ID = 0
# Loop through disk_map
for i, digit in enumerate(disk_map):
    size = int(digit)
    if i % 2 == 0:
        # File block: Add `size` instances of the file ID
        compact_file.append([file_ID] * size)
        file_ID += 1
    else:
        # Free space: Add `size` instances of free space (represented by '.')
        compact_file.append(['.'] * size)

# Remove empty lists
compact_file = [e for e in compact_file if e]

# Loop through files in reversed order
for i in range(len(compact_file) - 1, -1, -1):
    if not '.' in compact_file[i]:
        to_move = len(compact_file[i])
        # Find for free space from the left
        for j in range(len(compact_file)):
            if i > j:
                # Check if there is enough free space for this file
                free_space = compact_file[j].count('.')
                if free_space >= len(compact_file[i]):
                    
                    ID = compact_file[i][0]
                    # Replace free space with the fileID
                    for k in range(len(compact_file[j])):
                        if to_move > 0:
                            if compact_file[j][k] == '.':
                                compact_file[j][k] = ID
                                to_move -= 1
                                compact_file[i][to_move] = '.' # Mark the file's original position as free space
                                
# Calculate the checksum
checksum = 0
location = 0
for files in compact_file:
    for file in files:
        if file != '.':
            checksum += (int(file)*location)
        location +=1

print(f'Day 9.2: {checksum}')
                            
#%% Day 10
"""
A blank topographic map of the surrounding area (your puzzle input)
indicates the height at each position using a scale from 0 (lowest) to 9 (highest)
a hiking trail is any path that starts at height 0, ends at height 9, and 
always increases by a height of exactly 1 at each step. 
Hiking trails never include diagonal steps
a trailhead's score is the number of 9-height positions reachable from that trailhead via a hiking trail
What is the sum of the scores of all trailheads on your topographic map?
"""                        
sum_trailhead_scores = 0

# Get the map in lists inside list format

with open('fun_creations/advent_of_code/2024/data_day10t.txt') as data:
    map_grid = [[int(position) for position in line.strip()] for line in data]

# Get map dimensions
map_width, map_height = len(map_grid[0]), len(map_grid)

def check_neighbours(current_position,next_height):
    l, w = current_position
    neighbours = {}
    
    if w > 0 and map_grid[l][w-1] == next_height: neighbours['left'] = (l, w-1)
    if l > 0 and map_grid[l-1][w] == next_height: neighbours['up'] = (l-1, w)
    if w < map_width - 1 and map_grid[l][w+1] == next_height: neighbours['right'] = (l, w+1)
    if l < map_height - 1 and map_grid[l+1][w] == next_height: neighbours['down'] = (l+1, w)
    
    return neighbours

# look for possible trailhead
for l, line in enumerate(map_grid):
    for w, height in enumerate(line):
        if height == 0:
            trail_head = {0: [(l, w)]}
            
            # Check for a trail up to 9
            for i in range(1, 10):
                trail_head[i] = []
                for position in trail_head[i-1]:
                    neighbours = check_neighbours(position, i)
                    for spot in neighbours.values():
                        # For part 1 use this:
                        # if spot not in trail_head[i]:
                        #     trail_head[i].append(spot)
                        trail_head[i].append(spot)
            sum_trailhead_scores += len(trail_head[9])

print(f'Day 10.1: {sum_trailhead_scores}')
                
#%% Day 11
"""
Stones in a perfectly straight line, and each stone has a number engraved on it.
Every time you blink, the stones each simultaneously change according to the first applicable rule
-if 0: 0 = 1
-if even number of digits: stone replaced by two stones, digits devided over stones
-else: number multiplied by 2024

How many stones will you have after blinking 25 times?
"""
test = False

if test:
    stones = '125 17'
else:
    stones = '92 0 286041 8034 34394 795 8 2051489'

def blink(stones):
    """
    Every time you blink, the stones each simultaneously change according to
    rules.    
    """
    new_list_of_stones = ''
    for stone in stones.split():
        number_of_digits = len(str(stone))
        # if stone has 0 engraved, it's changed to a 1
        if int(stone) == 0:
            new_list_of_stones += '1 '
        
        # if digits is even, devide stone and digits        
        elif number_of_digits % 2 == 0:
            first_digit = int(stone[0:number_of_digits//2])
            second_digit = int((stone)[number_of_digits//2:])
            new_list_of_stones += str(first_digit) + ' ' + str(second_digit) + ' '
        # number multiplied by 2024       
        else:
            new_list_of_stones += str((int(stone)*2024)) + ' '

    return new_list_of_stones
    

for i in range(25):
    stones = blink(stones)
    print(25-1 -i)

    
number_of_stones = stones.split()
print(f'Day 11.1: {len(number_of_stones)}')

#%% Day 11 With grouping
from collections import defaultdict

test = False
blinks = 75

if test:
    start = '125 17'
else:
    start = '92 0 286041 8034 34394 795 8 2051489'

# Make a dict with counts of similar stones
stones = defaultdict(int) # defaultdict so that you can add to not yet existing keys
for stone in start.split():
    stones[int(stone)] += 1

def blink(stones):
    """
    Every time you blink, the stones each simultaneously change according to
    rules.    
    """
    new_stone_counts = defaultdict(int) # defaultdict so that you can add to not yet existing keys
    for stone, count in stones.items():
        number_of_digits = len(str(stone))
        # if stone has 0 engraved, it's changed to a 1
        if stone == 0:
            new_stone_counts[1] += count
            
        # if digits is even, devide stone and digits        
        elif number_of_digits % 2 == 0:
            first_digit = int(str(stone)[:number_of_digits//2])
            second_digit = int(str(stone)[number_of_digits//2:])
            new_stone_counts[first_digit] += count
            new_stone_counts[second_digit] += count
        # number multiplied by 2024       
        else:
            new_stone_counts[stone * 2024] += count

    return new_stone_counts
    

for i in range(blinks):
    stones = blink(stones)
    print(blinks - 1 -i)

    
# Output the number of stones after 75 blinks
total_stones = sum(stones.values())
print(f'Day 11.1: {total_stones}')

#%% Day 12
"""
puzzle input = a map of the garden plots
type of plants indicated by a single letter on your map
When multiple garden plots are growing the same type of plant and are touching 
(horizontally or vertically), they form a region.
regions can even appear within other regions
area = number of plots in region
perimeter = the number of sides of garden plots in the region that do not touch 
another garden plot in the same region.

price of fence = region's area * its perimeter.
"""
map_grid = []
with open('fun_creations/advent_of_code/2024/data_day12.txt') as data:
    map_grid = [[position for position in line.strip()] for line in data]

# Get map dimensions
max_l, max_w = len(map_grid), len(map_grid[0])
   
def check_neighbours(l, w, plant):
    region = []
    perimeter_cells = []
    neighbours = [(l,w)]
    added_plots.add((l,w))
    
    # While there are still neighbours to check, keep checking for new neighbours
    while neighbours:
        
        l, w = neighbours.pop()
        region.append((l,w))
        
        # Check all 4 possible directions (up, down, left, right)
        for dl, dw, direction in [(-1, 0, 'up'), (1, 0, 'down'), (0, -1, 'left'), (0, 1, 'right')]:
            nl, nw = l + dl, w + dw
            
            # Check if neighbour is still on the map
            if 0 <= nl < max_l and 0 <= nw < max_w:
                # Check if neighbour was not added already and if it has the same plant
                if (nl,nw) not in added_plots and map_grid[nl][nw] == plant:
                    added_plots.add((nl,nw))
                    neighbours.append((nl,nw))
                # If neighbour is a different plant, it needs a fence
                elif map_grid[nl][nw] != plant:
                    perimeter_cells.append((l,w,direction))
            # If it is an edge of the map, it needs a fence
            else:
                perimeter_cells.append((l,w,direction))
    return region, perimeter_cells


# Make a set to check if the plot is already added to a region
added_plots = set()
# Make a list of all separate regions
regions = []

# Loop through every spot on the map                
for l in range(max_l):
    for w in range(max_w):
        # Check if the plot is already added to a region
        if not (l,w) in added_plots:
            # Get the specific plant on that spot
            plant = map_grid[l][w]
            # Check all neighbours and find entire region containing the same plant type
            region, perimeter_cells = check_neighbours(l, w, plant)
            # Add new region to list of regions
            regions.append((plant,region, perimeter_cells))
            

total_fence_price = 0
# Calculate price of the fence around the regions
for plant, region, perimeter_cells in regions:
    area = len(region)
    perimeter = len(perimeter_cells)
    fence_price = area * perimeter
    
    total_fence_price += fence_price

print(f'Day 12.1: {total_fence_price}')
                

"""
new method of calculating the per-region price by multiplying the region's area 
by its number of sides.
"""    
# Depending on edge side, check if neighbour also has that edge
to_check = {'up': (0,1), 'right': (1,0), 'down': (0,1), 'left': (1,0)}
total_fence_price_2 = 0

# Loop through regions
for plant, region, perimeter_cells in regions:
    # If neighbour has the same edge, it is in the same side, so extract it from total fence
    minus_perimeter = 0
    
    # Loop through fence sides
    for l, w, direction in perimeter_cells:
        
        # depending on direction, check the specified neighbour
        dl, dw = to_check[direction]
        # Check if the neighbour also has a fence on the same side       
        if (l + dl, w + dw, direction) in perimeter_cells:
            # If so, it is part of the same side and should not be counted as a separate fence
            minus_perimeter += 1
    
    # Extract the perimeters that belong to a similar side, to get the number of sides
    sides = len(perimeter_cells) - minus_perimeter
    
    # Calculate the price of the fence for each region
    area = len(region)
    fence_price = area * sides
    # calculate the total fence price, based on sides instead of perimeters
    total_fence_price_2 += fence_price

print(f'Day 12.2: {total_fence_price_2}')
       
#%% Day 13
"""
Claw machines
it costs 3 tokens to push the A button and 1 token to push the B button.
You assemble a list of every machine's button behavior and prize location (your puzzle input)
what is the smallest number of tokens you would have to spend to win as many prizes as possible?
"""
from collections import defaultdict
import numpy as np

machines = defaultdict(list)
machine_counter = 0

# Get the data 
data = []
with open('fun_creations/advent_of_code/2024/data_day13.txt') as file:
    for line in file:
        data.append(line)

# Get info from the separate claw machines
for i, line in enumerate(data):
    # Every machine consists of 3 lines + an empty line
    if i % 4 == 0:
        # Get the button and prize parameters
        AdX , AdY = line.replace('Button A: X+','').replace(' Y+','').split(',')
        BdX , BdY = data[i+1].replace('Button B: X+','').replace(' Y+','').split(',')
        prizeX, prizeY = data[i+2].replace('Prize: X=','').replace(' Y=','').split(',')
        
        # Append to the dict
        machine_counter += 1
        machine = 'machine_' + str(machine_counter)
        machines[machine] += ((int(AdX) , int(AdY)),
                             (int(BdX) , int(BdY)),
                             (int(prizeX) , int(prizeY)))

def findA_B_presses(machine):
    # Get the parameters for thi machine                   
    (AdX , AdY), (BdX , BdY), (prizeX, prizeY) = machines[machine]

    # With numpy arrays
    # Coefficients matrix
    buttons = np.array([[AdX, BdX],
                        [AdY,  BdY]])    
    # Constants matrix
    prize = np.array([prizeX, prizeY])
    
    # Solve for [A, B]
    A, B = np.linalg.solve(buttons, prize)
    
    return round(A,2), round(B,2)

def findA_B_presses_2(machine):
    # Get the parameters for thi machine                   
    (AdX , AdY), (BdX , BdY), (prizeX, prizeY) = machines[machine]
    prizeX, prizeY = prizeX + 10000000000000 , prizeY + 10000000000000
      
    # By hand
    nBdX, nprizeX =  BdX* AdY, prizeX* AdY
    nBdY, nprizeY =  BdY* AdX, prizeY* AdX    
    B = (nprizeX - nprizeY) / (nBdX - nBdY)
    A = (prizeX - (BdX * B)) / AdX    
    return A,B

tokens = 0        
for machine in machines.keys():             
    A,B = findA_B_presses(machine)
    
    if A == int(A) and B == int(B) and A <= 100 and B <= 100:
        tokens += ((A*3) + (B))

print(f'Day 13.1: {int(tokens)}')

tokens = 0        
for machine in machines.keys():             
    A,B = findA_B_presses_2(machine)
    
    if A == int(A) and B == int(B):
        tokens += ((A*3) + (B))

print(f'Day 13.2: {int(tokens)}')

            
        
    
    
#%% Day 14
"""
puzzle input: a list of all of the robots' current positions (p=x,y) and 
velocities (v=x,y) in tiles per sec., one robot per line.
space is 101 tiles wide and 103 tiles tall
When a robot would run into an edge of the space they're in, they instead teleport to the other side
Where will the robots be after 100 seconds?
count the number of robots in each quadrant, multiply them to get safety factor
"""
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

# Dimensions of the space
test = False
if test:
    space = (11, 7) #(wide, tall)
else:
    space = (101, 103)

robots = defaultdict(list)
# Get robot data
with open('fun_creations/advent_of_code/2024/data_day14.txt') as file:
    for i, line in enumerate(file):
        # Get rid of enters
        line = line.strip()
        # Separate position and velocity
        position, velocity = line.replace('p=','').replace(' v=',';').split(';')
        pX, pY = position.split(',')
        vX, vY = velocity.split(',')
        # Add to robots dictionary
        robots['robot_' + str(i+1)] = ((int(pX),int(pY)), (int(vX),int(vY)))

def robot_walk(robots):
    # For each robot
    for robot, robot_info in robots.items():
        # Get current_position and velocity info
        (cpX,cpY) , (vX,vY) = robot_info
        
        # Get robot to new position
        nX = cpX + vX
        if nX < 0:
            nX = space[0] + nX
        elif nX > space[0] -1:
            nX = nX - space[0]
        
        nY = cpY + vY
        if nY < 0:
            nY = space[1] + nY
        elif nY > space[1] -1:
            nY = nY - space[1]
        
        # Update dict with new position
        robots[robot] = ((nX,nY), (vX,vY))

def robots_per_quadrant(robots):
    # Define quadrants
    quadrants = {'quadrant_1' : ( (0,int(space[0]/2)-1) , (0,int(space[1]/2)-1) ,0),
                 'quadrant_2' : ( (int(space[0]/2)+1,space[0]-1) , (0,int(space[1]/2)-1) ,0),
                 'quadrant_3' : ( (0,int(space[0]/2)-1), (int(space[1]/2)+1,space[1]-1) ,0),
                 'quadrant_4' : ( (int(space[0]/2)+1,space[0]-1), ((int(space[1]/2)+1), space[1]-1),0)
                     }
    
    # Check for each robot in which quadrant it is       
    for robot, robot_info in robots.items():
        # Get current_position and velocity info
        (pX,pY) , (vX,vY) = robot_info
        # Loop through quadrants
        for quadrant, boundaries in quadrants.items():
            (xmin,xmax),(ymin,ymax),robots = boundaries
            # Check if robot is in that quadrant
            if xmin <= pX <= xmax and ymin <= pY <= ymax:
                # If so, add to the robot counter
                robots += 1
                quadrants[quadrant] = ((xmin,xmax),(ymin,ymax),robots)
    
    # Calculate safety factor
    safety_factor = 1
    quadrant_robots = defaultdict(int)
    for quadrant, boundaries in quadrants.items():
        (xmin,xmax),(ymin,ymax),robots = boundaries
        safety_factor = safety_factor * robots
        quadrant_robots[quadrant] = robots
        
    # If Xmas tree, then Q1 and Q2 should be mirrors, so similar robots and Q3 and Q4 also
    christmas_tree = False
    if quadrant_robots['quadrant_1'] == quadrant_robots['quadrant_2'] and quadrant_robots['quadrant_3'] == quadrant_robots['quadrant_4']:
        christmas_tree = True
        
    return safety_factor, christmas_tree

# Let robots walk for 100 sec
for i in range(100):
    robot_walk(robots)
safety_factor, christmas_tree = robots_per_quadrant(robots)

print(f'Day 14.1: {safety_factor}')

# Find Xmas tree (where safety_factor = lowest)
sec = 0  
for i in range(7000):
    sec += 1
    robot_walk(robots)
    # Get saftey_facor
    safety_factor, christmas_tree = robots_per_quadrant(robots)
    
    if i == 0:
        lowest_safety_factor = safety_factor
    else:
        if safety_factor < lowest_safety_factor:
            lowest_safety_factor = safety_factor
            sec_lowest_safety = sec

print(f'Day 14.2: {sec_lowest_safety}')

#%% Day 15      
"""
your puzzle input = map of the warehouse and a list of movements the robot will attempt to make
robot (@)
boxes (O)
wall (#)
if there are any boxes (O) in the way, the robot will also attempt to push those boxes. 
However, if this action would cause the robot or a box to move into a wall (#), 
nothing moves instead.
GPS coordinate of a box is equal to 100 times its distance from the top edge of the map plus its distance from the left edge of the map.
"""     
from collections import deque 
 
warehouse_map = []
movements = ''
# Get the data and separate between map and movemeents
with open('fun_creations/advent_of_code/2024/data_day15t1.txt') as file:
    for i, line in enumerate(file):
        
        # Get the map of the warehouse ou tof the data
        if line.startswith('#'):
            row = []
            for j, character in enumerate(line.strip()):
                row.append(character)
                # Get start_point of robot
                if character == '@':
                    start_point = (i,j)
            warehouse_map.append(row)
        
        # Get list of movements out
        else:
            for character in line.strip():
                movements += character
# Get map boundaries
map_width, map_height = (len(warehouse_map[0]), len(warehouse_map))

# Def for finding the next position of the robot
def get_next_position(current_pos, movement):
    """Calculate next position"""
    row, col = current_pos
    moves = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
        '[': (0, 1),
        ']': (0, -1)
    }
    delta_row, delta_col = moves[movement]
    return (row + delta_row, col + delta_col)

# Let the robot move
current_position = start_point
for movement in movements:
    # Trying to move to
    y,x = get_next_position(current_position, movement)

    # If there is no wall or box, walk that way
    if warehouse_map[y][x] == '.':
        warehouse_map[y][x] = '@'        
        warehouse_map[current_position[0]][current_position[1]] = '.'
        current_position = (y,x)

    # If there is a box, check what's behind it
    elif warehouse_map[y][x] == 'O':
        ny, nx = y, x
        while True:         
            ny,nx = get_next_position((ny,nx), movement)
            # If there is space behind it, move all boxes between @ and .
            if warehouse_map[ny][nx] == '.':
                warehouse_map[ny][nx] = 'O'
                warehouse_map[y][x] = '@'                
                warehouse_map[current_position[0]][current_position[1]] = '.'
                current_position = (y,x)
                break
            # If there is a wall, do nothing
            elif warehouse_map[ny][nx] == '#':
                break

# For each box, calculate GPS coordinate (100*y + x)
sum_of_GPS_coordinates = 0
for y, row in enumerate(warehouse_map):
    for x, spot in enumerate(row):
        # Check if it's a box
        if spot == 'O':
            sum_of_GPS_coordinates += (y*100) + x

print(f'Day 15.1: {sum_of_GPS_coordinates}')


# Day 15.2 Does not work!!!

warehouse_map_2 = []
# Get the data and separate between map and movemeents
with open('fun_creations/advent_of_code/2024/data_day15t1.txt') as file:
    for i, line in enumerate(file):
        
        # Get the map of the warehouse ou tof the data
        if line.startswith('#'):
            row = []
            for j, character in enumerate(line.strip()):
                if character == '@':
                    # Get start_point of robot
                    start_point = (i,len(row))
                    row.append(character)
                    row.append('.')
                elif character == 'O':
                    row.append('[')
                    row.append(']')
                else:
                    row.append(character)
                    row.append(character)
            warehouse_map_2.append(row)

# Let the robot move
current_position = start_point
for movement in movements:
    # Trying to move to
    y,x = get_next_position(current_position, movement)
    new_position = (y,x)

    # If there is no wall or box, walk that way
    if warehouse_map_2[y][x] == '.':
        warehouse_map_2[y][x] = '@'        
        warehouse_map_2[current_position[0]][current_position[1]] = '.'
        current_position = new_position

    # If there is a box, check what's behind it
    elif warehouse_map_2[y][x] == '[' or warehouse_map_2[y][x] == ']' or warehouse_map_2[y][x] == 'O':
        ny, nx = y, x        
                             
        # If moving sideways, box is 2 spots big, so check one spot further
        if movement in "<>":
            while True:
                ny,nx = get_next_position((ny,nx), movement)
                warehouse_map_2[y][x] = 'O'
                warehouse_map_2[ny][nx] = 'O'
                nny,nnx = get_next_position((ny,nx), movement)
                            
                # If there is space behind it, move all boxes between @ and .
                if warehouse_map_2[nny][nnx] == '.':                   
                    warehouse_map_2[nny][nnx] = 'O'
                    warehouse_map_2[y][x] = '@'
                    warehouse_map_2[current_position[0]][current_position[1]] = '.'                    
                    current_position = (y,x)
                    # Fix the boxes
                    counter = 0
                    for i, spot in enumerate(warehouse_map_2[y]):
                        if spot == 'O':
                            counter += 1
                            if counter % 2 == 0:
                                warehouse_map_2[y][i] = ']'
                            else:
                                warehouse_map_2[y][i] = '['                            
                    break
                                                     
                # If there is a wall behind it, do nothing
                elif warehouse_map_2[nny][nnx] == '#':
                    break
                # change to 'O' to easily fix later
                else:
                    warehouse_map_2[nny][nnx] = 'O'

        # If moving up or down, 1 box can move 2 boxes above or below
        if movement in '^v':
            y1,x1 = y,x
            y2,x2 = get_next_position((y1,x1), warehouse_map_2[y1][x1] )
            boxes_to_push = set(((y1,x1),(y2,x2)))
            boxes_to_check = set(((y1,x1),(y2,x2)))
            
            while boxes_to_check:
                box = boxes_to_check.pop()
                side1, side2 = box[0], box[1]
                # Check what is in front of both sides
                a1,b1 = get_next_position((side1[0],side1[1]), movement)
                a2,b2 = get_next_position((side2[0],side2[1]), movement)           
                
                # If this box would be pushed into a wall
                if warehouse_map_2[a1][b1] == '#' or warehouse_map_2[a2][b2] == '#':
                    # Don't push any boxes, and stop trying to
                    boxes_to_check.clear()
                    boxes_to_push.clear()
                    break
                
                # If this box would be pushed into another box
                elif warehouse_map_2[a1][b1] in '[]' or warehouse_map_2[a2][b2] in '[]':
                    boxes_to_push.add(box)                                                
                    # find other halve of the box(es)
                    if warehouse_map_2[a1][b1] in '[]':
                        a1b, b1b = get_next_position((a1,b1), warehouse_map_2[a1][b1])
                        boxes_to_check.add(((a1,b1),(a1b,b1b)))
                    if warehouse_map_2[a2][b2] in '[]':
                        a2b, b2b = get_next_position((a2,b2), warehouse_map_2[a2][b2])
                        boxes_to_check.add(((a2,b2),(a2b,b2b)))
                    
        # Move
        # If no boxes would be pushed
        if not boxes_to_push:
            # Don't move the robot
            continue
        # If boxes have to be pushed
        boxes_to_push = list(boxes_to_push)
        for box in reversed(boxes_to_push):
            for side in box:
                y,x = side
                ny,nx = get_next_position((y,x), movement)
                warehouse_map_2[ny][nx] = warehouse_map_2[y][x]
                warehouse_map_2[y][x] = '.'
        # replace robot
        warehouse_map_2[new_position[0]][new_position[1]] = '@'        
        warehouse_map_2[current_position[0]][current_position[1]] = '.'
        current_position = new_position

    elif warehouse_map_2[y][x] == '#':
        break
               
    
    for line in warehouse_map_2:
        print(line)
    print()
#%% Day 16
"""
Reindeer Maze. S = Start, E = end
Reindeer can move forward one tile at a time (increasing their score by 1 point), 
but never into a wall (#). They can also rotate clockwise or counterclockwise 
90 degrees at a time (increasing their score by 1000 points).
Get the loweest score to the end
"""

# Get the maze 
maze = []
with open('fun_creations/advent_of_code/2024/data_day16t1.txt') as file:
    for i, line in enumerate(file):
        row = []
        for j, character in enumerate(line.strip()):
            row.append(character)
            # Get start_point of the reindeer
            if character == 'S':
                start_point = (i,j)            
        maze.append(row)

next_step = {'E': (0,1),
             'W': (0,-1),
             'N': (1,0),
             'S': (-1,0)}



    
    
    
    