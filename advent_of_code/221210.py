"""
https://adventofcode.com/2022/day/10

Consider a simple CPU that are both driven by a precise clock circuit. The 
clock circuit ticks at a constant rate; each tick is called a cycle.

Start by figuring out the signal being sent by the CPU. 
The CPU has a single register, X, which starts with the value 1. 
It supports only two instructions:
- addx V takes two cycles to complete. After two cycles, the X register is 
increased by the value V. (V can be negative.)
- noop takes one cycle to complete. It has no other effect.

consider the signal strength (the cycle number multiplied by the value of the 
X register) during the 20th cycle and every 40 cycles after that 
(that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).
"""

# Read the file and make a list of all instructions
instructions = []
with open('221210.txt') as file:
        for line in file:
            instructions.append(line.strip())

#%% part 1 
# What is the sum of the six signal strengths?
X = 1 
cycle = 0
sum_X = 0
# Loop through the instructions
for instruction in instructions:
    # When instruction is noop, add a cycle
    if instruction == 'noop':
        cycle += 1
        
        # if the cycle is 20, 60 etc.. determine the signal strength
        if (cycle == 20 or
            cycle == 60 or
            cycle == 100 or
            cycle == 140 or
            cycle == 180 or
            cycle == 220):
            print("cycle " + str(cycle) + ": " + str(X))
            # sum the six signal strengths
            sum_X += (X * cycle)
    
    # When instruction is addx, first add 2 cycles
    if 'addx' in instruction:
        cycle += 1
        if (cycle == 20 or
            cycle == 60 or
            cycle == 100 or
            cycle == 140 or
            cycle == 180 or
            cycle == 220):
            print("cycle " + str(cycle) + ": " + str(X))
            sum_X += (X * cycle)
        
        cycle += 1
        if (cycle == 20 or
            cycle == 60 or
            cycle == 100 or
            cycle == 140 or
            cycle == 180 or
            cycle == 220):
            print("cycle " + str(cycle) + ": " + str(X))
            sum_X += (X * cycle)
        
        # determine what value to add
        to_add = int(instruction.split(' ')[1])
        # Change X accordingly
        X += to_add      

print(sum_X)
#%% part 2
"""
The X register controls the horizontal position of a sprite.

The sprite is 3 pixels wide, and the X register sets the horizontal position 
of the middle of that sprite.

The pixels on the CRT: 40 wide and 6 high:
Cycle   1 -> ######################################## <- Cycle  40
Cycle  41 -> ######################################## <- Cycle  80
Cycle  81 -> ######################################## <- Cycle 120
Cycle 121 -> ######################################## <- Cycle 160
Cycle 161 -> ######################################## <- Cycle 200
Cycle 201 -> ######################################## <- Cycle 240

The CRT draws a single pixel during each cycle.
If the sprite is positioned such that one of its three pixels is the pixel 
currently being drawn, the screen produces a lit pixel (#); otherwise, the 
screen leaves the pixel dark (.).
"""
def drawing(CRT_high, CRT_wide, X):    
    
    # Check position of sprite
    sprite = [X-1, X, X+1]
    
    # Check if CRT and sprite overlap and determine if pixel is drawn
    if CRT_wide in sprite:
        pixel = '#'
    else:
        pixel = '.'
    
    # Draw the appropriate pixel
    CRTs[CRT_high].append(pixel)
       
    # Every 40 cycles, go to next CRT lane
    CRT_wide += 1
    if CRT_wide == 40:
        CRT_high += 1
        CRT_wide = 0
    
    return CRT_high, CRT_wide

X = 1 
cycle = 0        
CRT_high = 0
CRT_wide = 0

CRT_1 = []
CRT_2 = []
CRT_3 = []
CRT_4 = []
CRT_5 = []
CRT_6 = []
CRTs = [CRT_1, CRT_2, CRT_3, CRT_4, CRT_5, CRT_6]     
    
for instruction in instructions:
    # When instruction is noop, add a cycle
    if instruction == 'noop':
        cycle += 1
        CRT_high, CRT_wide = drawing(CRT_high, CRT_wide, X)        
    
    # When instruction is addx, first add 2 cycles
    if 'addx' in instruction:
        cycle += 1
        CRT_high, CRT_wide = drawing(CRT_high, CRT_wide, X)
        
        cycle += 1
        CRT_high, CRT_wide = drawing(CRT_high, CRT_wide, X)
        
        # determine what value to add
        to_add = int(instruction.split(' ')[1])
        # Change X accordingly
        X += to_add

# Make the image
for CRT in CRTs:
    CRT_string = ''
    for pixel in CRT:
        CRT_string += pixel
    with open("221210_result.txt", "a") as file_object:
        file_object.write(str(CRT_string) + '\n')        
        
        


