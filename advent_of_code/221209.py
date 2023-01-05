"""
https://adventofcode.com/2022/day/9

Consider a rope with a knot at each end; these knots mark the head and the tail 
of the rope. If the head moves far enough away from the tail, the tail is 
pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to model 
the positions of the knots on a two-dimensional grid. Then, by following a 
hypothetical series of motions (your puzzle input) for the head, you can 
determine how the tail will move.

the head (H) and tail (T) must always be touching (diagonally adjacent and even 
overlapping both count as touching)
If the head is ever two steps directly up, down, left, or right from the tail, 
the tail must also move one step in that direction so it remains close enough.
if the head and tail aren't touching and aren't in the same row or column, the 
tail always moves one step diagonally to keep up

After each step, you'll need to update the position of the tail if the step 
means the head is no longer adjacent to the tail.

== Initial State ==

  123456
5 ......
4 ......
3 ......
2 ......
1 H.....  (H covers T, s)

"""
# Simulate your complete hypothetical series of motions. 
# How many positions does the tail of the rope visit at least once?

# Indiciate starting position
starting_position_row = '6'
starting_position_column = '12'
tail_positions = []

# Read the file and make a list of all steps
steps = []
with open('221209.txt') as file:
        for line in file:
            steps.append(line.strip())          

#%% Part 1
# WHat is the current position of both knots
current_position_head_row = starting_position_row
current_position_head_column = starting_position_column
current_position_tail_row = starting_position_row
current_position_tail_column = starting_position_column

# Loop through the steps and update position of H
for step in steps:
    direction = step.split(' ')[0]
    number_of_steps = step.split(' ')[1]
    for i in range(int(number_of_steps)):
        current_row_H = int(current_position_head_row)
        current_column_H = int(current_position_head_column)
        if direction == 'R':
            current_column_H += 1
        elif direction == 'L':
            current_column_H -= 1
        elif direction == 'U':
            current_row_H += 1
        elif direction == 'D':
            current_row_H -= 1
        
        current_position_head_row = current_row_H 
        current_position_head_column = current_column_H
        print("head: " + str(current_position_head_row) + str(current_position_head_column))
        
        # Where is the tail now
        current_row_T = int(current_position_tail_row)
        current_column_T = int(current_position_tail_column)
        
        # If the head is ever two steps directly up, down, left, or right from 
        # the tail, the tail must also move one step in that direction so it 
        # remains close enough.
        if current_row_T == current_row_H:
            if current_column_T + 1 < current_column_H:
                current_column_T += 1                
            elif current_column_H < current_column_T - 1:
                current_column_T -= 1
        elif current_column_T == current_column_H:
            if current_row_T + 1 < current_row_H:
                current_row_T += 1               
            elif current_row_H < current_row_T - 1:
                current_row_T -= 1
        
        # if the head and tail aren't touching and aren't in the same row or
        # column, the tail always moves one step diagonally to keep up
        else:
            if (current_row_T - current_row_H > 1 or
                current_row_T - current_row_H < -1 or
                current_column_T - current_column_H > 1 or
                current_column_T - current_column_H < -1):

                if current_row_T < current_row_H:
                    current_row_T += 1
                else:
                    current_row_T -= 1
                if current_column_T < current_column_H:
                    current_column_T += 1
                else:
                    current_column_T -= 1
                
        current_position_tail_row = str(current_row_T) 
        current_position_tail_column = str(current_column_T)
        
        current_position_tail = current_position_tail_row + current_position_tail_column
        print("tail: " + str(current_position_tail))
        
        tail_positions.append(current_position_tail)

print("The tail visits " + str(len(set(tail_positions))) + " positions")
        

#%% Part 2
# Rather than two knots, you now must simulate a rope consisting of ten knots. 
# One knot is still the head of the rope and moves according to the series of 
# motions. Each knot further down the rope follows the knot in front of it 
# using the same rules as before.

# What is the current position of the 10 knots
knots = ['head', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'tail']
knots_positions = {}
for knot in knots:
    knots_positions[knot] = [starting_position_row, starting_position_column]

# Loop through the steps and update position of H
for step in steps:
    direction = step.split(' ')[0]
    number_of_steps = step.split(' ')[1]
    for i in range(int(number_of_steps)):
        current_row_H = int(knots_positions['head'][0])
        current_column_H = int(knots_positions['head'][1])
        if direction == 'R':
            current_column_H += 1
        elif direction == 'L':
            current_column_H -= 1
        elif direction == 'U':
            current_row_H += 1
        elif direction == 'D':
            current_row_H -= 1
        
        knots_positions['head'] = [current_row_H, current_column_H]
                
        # Where are the other knots now
        for knot in knots_positions:
            if knot != 'head':
                current_row = int(knots_positions[knot][0])
                current_column = int(knots_positions[knot][1])
                
                # Check position of the knot before the current knot
                knot_index = knots.index(knot)
                previous_knot = knots[knot_index -1]
                previous_knot_row = int(knots_positions[previous_knot][0])
                previous_knot_column = int(knots_positions[previous_knot][1])
                       
                # If the knot is ever two steps directly up, down, left, or right 
                # from the previous knot, the tail must also move one step in that 
                # direction so it remains close enough.
                if current_row == previous_knot_row:
                    if current_column + 1 < previous_knot_column:
                        current_column += 1                
                    elif previous_knot_column < current_column - 1:
                        current_column -= 1
                elif current_column == previous_knot_column:
                    if current_row + 1 < previous_knot_row:
                        current_row += 1               
                    elif previous_knot_row < current_row - 1:
                        current_row -= 1
            
                # if the head and tail aren't touching and aren't in the same row or
                # column, the tail always moves one step diagonally to keep up
                else:
                    if (current_row - previous_knot_row > 1 or
                        current_row - previous_knot_row < -1 or
                        current_column - previous_knot_column > 1 or
                        current_column - previous_knot_column < -1):
        
                        if current_row < previous_knot_row:
                            current_row += 1
                        else:
                            current_row -= 1
                        if current_column < previous_knot_column:
                            current_column += 1
                        else:
                            current_column -= 1
                    
                knots_positions[knot] = [current_row, current_column]
                
                if knot == 'tail':
                    current_position_tail = str(current_row) + ' ' + str(current_column)
                    tail_positions.append(current_position_tail)

    print("head: " + str(current_row_H) + ' ' + str(current_column_H))
    print("tail: " + str(current_position_tail))
                
                    

print("The tail visits " + str(len(set(tail_positions))) + " positions")
        
            
                
            
                
        
            
            
            

            
        
    
    
    
    