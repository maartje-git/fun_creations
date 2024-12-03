"""
https://adventofcode.com/2022/day/6

To be able to communicate with the Elves, the device needs to lock on to their 
signal. The signal is a series of seemingly-random characters that the device 
receives one at a time.

To fix the communication system, you need to add a subroutine to the device 
that detects a start-of-packet marker in the datastream. 
In the protocol being used by the Elves, the start of a packet is indicated by 
a sequence of four characters that are all different.

your subroutine needs to identify the first position where the four most 
recently received characters were all different. 
Specifically, it needs to report the number of characters from the beginning of 
the buffer to the end of the first such four-character marker.
""" 

# How many characters need to be processed before the first start-of-packet 
# marker is detected?

with open('221206.txt') as file:
    # Make string out of data
    for signal in file:
        # Loop through signal
        for i, character in enumerate(signal):
            # after there are at least 4 characters passed
            if i > 2:
                # cut out every next 4 characters
                four_characters = signal[i-3:i+1]
                # Make a set out of the four_characters, sets cannot have 
                # duplicate values
                four_characters_set = set(four_characters)
                # Check if the set is 4 characters long, because then they are
                # unique
                set_lenght = len(four_characters_set)
                if set_lenght == 4:
                    print(i+1)
                    break
# A start-of-message marker is just like a start-of-packet marker, 
# except it consists of 14 distinct characters rather than 4.
# How many characters need to be processed before the first start-of-message 
# marker is detected?           
                        
with open('221206.txt') as file:
    # Make string out of data
    for signal in file:
        # Loop through signal
        for i, character in enumerate(signal):
            # after there are at least 4 characters passed
            if i > 13:
                # cut out every next 4 characters
                fourteen_characters = signal[i-13:i+1]
                # Make a set out of the four_characters, sets cannot have 
                # duplicate values
                fourteen_characters_set = set(fourteen_characters)
                # Check if the set is 4 characters long, because then they are
                # unique
                set_lenght = len(fourteen_characters_set)
                if set_lenght == 14:
                    print(i+1)
                    break               
        

                