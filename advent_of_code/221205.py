"""
https://adventofcode.com/2022/day/5

Supplies are stored in stacks of marked crates, but because the needed supplies 
are buried under many other crates, the crates need to be rearranged.
The crane operator will rearrange them in a series of carefully-planned steps.
Crates are moved one at a time.
The Elves just need to know which crate will end up on top of each stack.
"""

# After the rearrangement procedure completes, 
# what crate ends up on top of each stack?
import pandas as pd

crates = pd.DataFrame()
df = pd.DataFrame()

with open('221205.txt') as file:
    
    # Make dataframe with room for 9 stacks
    for i in range(9):
        stack = 'stack_' + str(i+1)
        crates = crates.append({'stack': stack,
                                'crates': ''}, ignore_index=True)
    
    # Find the crates per stack and make a string out of it.
    for i in range(8):
        line = next(file)
        ## The first 8 lines of the file are crates 
        
        # make an empty list to append characters of a line from the file to
        characters = []
        # start a counter to count which stack a crate belongs to
        # Start at -1, so that the first +1 makes 0, to use as index
        counter = -1
        
        # Loop through each line with crates
        for j, character in enumerate(line):
            # Every 4th character in the line is a crate
            if (j-1)%4 == 0:
                # Every crate belongs to the next stack
                counter = counter + 1
                
                # Get the already stacked crates from previous lines from the df
                stacked_crates = crates['crates'][counter]
                # Add the just obtained crate to the stack
                stacked_crates = stacked_crates + character
                # Add the stack including the newest crate to the df
                crates.at[counter, 'crates'] = stacked_crates.strip()
                  ## Stripped from empty spaces
    
    # Make an empty list to append moves of the crane to
    moves = []
    # Loop through the lines of the file and append the moves
    for i, line in enumerate(file):
        if i > 1:
            move = line
            moves.append(move)

# # If the crane moves only 1 box at the time
# # Loop through moves
# for i, move in enumerate(moves):
#     # from each move extract the 3 different digits
#     numbers = [int(number) for number in move.split() if number.isdigit()]
#     # From those digits, extract the number of crates to move
#     crates_to_move = numbers[0]
#     # Extract the stack of crates from the stack where to move crates from
#     start_stack_row = crates[
#         crates['stack'] == 'stack_'+ str(numbers[1])].reset_index()
#     # Extract the stack of crates from the stack where to move crates to
#     end_stack_row = crates[
#         crates['stack'] == 'stack_'+ str(numbers[2])].reset_index()

#     # Get the string of crates only
#     start_stack = start_stack_row['crates'][0]
#     end_stack = end_stack_row['crates'][0]
    
#     # For every crate that needs to be moved       
#     for i in range(int(crates_to_move)):
#         # Add the crate to the stack where it should move to
#         end_stack = start_stack[0] + end_stack
#         # Remove it from the stack where it is moved from
#         start_stack = start_stack[1:]

#     # Change the stacks of crates in the df            
#     crates.at[numbers[1]-1, 'crates'] = start_stack
#     crates.at[numbers[2]-1, 'crates'] = end_stack

# # what crate ends up on top of each stack?            
# answer = ''
# for stack in crates['crates']:
#     answer = answer + stack[0]
# print(answer)

# The crane has the ability to pick up and move multiple crates at once.
# After the rearrangement procedure completes
# what crate ends up on top of each stack?

# If the crane moves multiple boxes at the time

# Loop through moves
for i, move in enumerate(moves):
    # from each move extract the 3 different digits
    numbers = [int(number) for number in move.split() if number.isdigit()]
    # From those digits, extract the number of crates to move
    crates_to_move = numbers[0]
    # Extract the stack of crates from the stack where to move crates from
    start_stack_row = crates[
        crates['stack'] == 'stack_'+ str(numbers[1])].reset_index()
    # Extract the stack of crates from the stack where to move crates to
    end_stack_row = crates[
        crates['stack'] == 'stack_'+ str(numbers[2])].reset_index()

    # Get the string of crates only
    start_stack = start_stack_row['crates'][0]
    end_stack = end_stack_row['crates'][0]
    
    # Add the crates  to the stack where it should move to
    end_stack = start_stack[0:crates_to_move] + end_stack
    # Remove the crates  to the stack where it should move from
    start_stack = start_stack[crates_to_move:]
   
    # Change the stacks of crates in the df
    crates.at[numbers[1]-1, 'crates'] = start_stack
    crates.at[numbers[2]-1, 'crates'] = end_stack

# what crate ends up on top of each stack?              
answer = ''
for stack in crates['crates']:
    answer = answer + stack[0]
print(answer)

