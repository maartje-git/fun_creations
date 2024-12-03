"""
https://adventofcode.com/2022/day/2

The first column is what your opponent is going to play: 
A for Rock, B for Paper, and C for Scissors.

The second column, you reason, must be what you should play in response: 
X for Rock, Y for Paper, and Z for Scissors.

Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round 
(0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

# What would your total score be 
# if everything goes exactly according to your strategy guide?

import pandas as pd
# Append the two characters per line of the data file to a df
df = pd.read_csv(
    '221202.txt', 
    sep=' ', 
    header=None, 
    names=['opponent', 'you'])

# Add 2 new columns to the df
df['shape_score'] = ''
df['score'] = ''

# Loop through the df
for x in df.index:
    # For every line identify your and your opponents hand shape
    your_shape = df['you'][x]
    opponent_shape = df['opponent'][x]
    
    # Assign shape_scores and win/draw/lose scores
    # if you have rock
    if your_shape == 'X':
        shape_score = 1
        # if your opponent has rock
        if opponent_shape == 'A':
            score = 3
        # if your opponent has paper
        elif opponent_shape == 'B':
            score = 0
        # if your opponent has scissors
        elif opponent_shape == 'C':
            score = 6
    # if you have paper
    elif your_shape == 'Y':
        shape_score = 2
        # if your opponent has rock
        if opponent_shape == 'A':
            score = 6
        # if your opponent has paper
        elif opponent_shape == 'B':
            score = 3
        # if your opponent has scissors
        elif opponent_shape == 'C':
            score = 0
    # If you have scissors
    elif your_shape == 'Z':
        shape_score = 3
        # if your opponent has rock
        if opponent_shape == 'A':
            score = 0
        # if your opponent has paper
        elif opponent_shape == 'B':
            score = 6
        # if your opponent has scissors
        elif opponent_shape == 'C':
            score = 3
    # For every line, fill in the appropriate scores
    df.at[x,'shape_score'] = shape_score
    df.at[x,'score'] = score

# calculate the total score    
print(sum(df['shape_score']) + sum(df['score']))

# the second column says how the round needs to end: 
# X means you need to lose, Y means you need to end the round in a draw, 
# and Z means you need to win.

# Add 2 more columns to the df
df['shape_score2'] = ''
df['score2'] = ''

# Loop through the df
for x in df.index:
    # For every line identify your and your opponents hand shape
    end = df['you'][x]
    opponent_shape = df['opponent'][x]
    
    # Assign win/draw/lose scores, determine your hand shape based on opponents
    # hand shape and assign shape_score
    # You lose
    if end == 'X':
        score = 0
        # if your opponent has rock
        if opponent_shape == 'A':
            # you have scissors
            shape_score = 3
        # if your opponent has paper
        elif opponent_shape == 'B':
            # you have rock
            shape_score = 1
        # if your opponent has scissors
        elif opponent_shape == 'C':
            # you have paper
            shape_score = 2
    # you play a draw
    elif end == 'Y':
        score = 3
        # if your opponent has rock
        if opponent_shape == 'A':
            # you have rock
            shape_score = 1
        # if your opponent has paper
        elif opponent_shape == 'B':
            # you have paper
            shape_score = 2
        # if your opponent has scissors
        elif opponent_shape == 'C':
            # you have scissors
            shape_score = 3
    # you win
    elif end == 'Z':
        score = 6
        # if your opponent has rock
        if opponent_shape == 'A':
            # you have paper
            shape_score = 2
        # if your opponent has paper
        elif opponent_shape == 'B':
            # you have scissors
            shape_score = 3
        # if your opponent has scissors
        elif opponent_shape == 'C':
            # you have rock
            shape_score = 1
    
    # For every line fill in the appropriate score
    df.at[x,'shape_score2'] = shape_score
    df.at[x,'score2'] = score

# Calculate total score    
print(sum(df['shape_score2']) + sum(df['score2']))    
        
    
