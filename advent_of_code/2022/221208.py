"""
https://adventofcode.com/2022/day/8

The elves are curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house 
hidden.

data = a map with the height of each tree
Each tree is represented as a single digit whose value is its height, 
where 0 is the shortest and 9 is the tallest.
A tree is visible if all of the other trees between it and an edge of the grid 
are shorter than it. Only consider trees in the same row or column.
"""

# Consider your map; how many trees are visible from outside the grid?

# start a counter to count visible trees
tree_counter = 0

# Read the file and make a list of all tree rows
rows = []
with open('221208.txt') as file:
    #  append rows to list
    for line in file:
        rows.append(line.strip())

# Make a list with all tree columns
columns = ['']*len(rows[1]) # Make a list with number of items = len(row)
for row in rows:
    for i, tree in enumerate(row):
        column = columns[i]
        columns[i] = column + tree

# Check for each tree whether they are visible
# loop through rows
for j, row in enumerate(rows):
    # Loop through trees in each row
    for k, tree in enumerate(row):
        # starting point = it's not an outer tree
        outer_tree = False
        
        # which tree are you looking at
        current_tree_height = tree
        # What trees are on eithter side of the current tree
        trees_left = row[:k]
        trees_right = row[k+1:]
        
        # Check what the highest tree is on either side
        # If that does not work, it is an outer-tree
        try:
            heighest_tree_left = max(trees_left)
        except:
            outer_tree = True
        try:
            heighest_tree_right = max(trees_right)
        except:
            outer_tree = True
        
        # If the current tree is an outer tree, count it as visible
        if outer_tree:
            tree_counter = tree_counter + 1
            
        # If it's not an outer tree, check if there are any heigher trees on
        # either side
        else:
            # If there is no heigher tree on either side, the current tree
            # is visible
            if (current_tree_height > heighest_tree_left or
                current_tree_height > heighest_tree_right):
                tree_counter = tree_counter + 1
            # If it is not visible to either side, check if it's visible up or
            # down
            else:
                # Go to the appropriate location in the columns
                column = columns[k]
                tree = column[j]
                
                outer_tree = False
                
                # which tree are you looking at
                current_tree_height = tree
                # What trees are on eithter side of the current tree
                trees_up = column[:j]
                trees_down = column[j+1:]
                
                # Check what the highest tree is on either side
                # If that does not work, it is an outer-tree
                try:
                    heighest_tree_up = max(trees_up)
                except:
                    outer_tree = True
                try:
                    heighest_tree_down = max(trees_down)
                except:
                    outer_tree = True
                
                # If the current tree is an outer tree, count it as visible
                if outer_tree:
                    tree_counter = tree_counter + 1
                    
                # If it's not an outer tree, check if there are any heigher trees on
                # either side
                else:
                    # If there is no heigher tree on either side, the current tree
                    # is visible
                    if (current_tree_height > heighest_tree_up or
                        current_tree_height > heighest_tree_down):
                        tree_counter = tree_counter + 1
print('how many trees are visible from outside the grid? ' + str(tree_counter))               
                
# A tree's scenic score is found by multiplying together its viewing distance 
# in each of the four directions.
# Consider each tree on your map. What is the highest scenic score possible for 
# any tree?

# Calculate scenic score for each tree
scenic_scores = []
# loop through rows
for j, row in enumerate(rows):
    # Loop through trees in each row
    for k, tree in enumerate(row):
        # What trees are on eithter side of the current tree
        trees_left = row[:k]
        trees_right = row[k+1:]
        
        # start a viewing distance meter for each side
        viewing_distance_left = 0
        viewing_distance_right = 0
        viewing_distance_up = 0
        viewing_distance_down = 0
        
        ## Count viewing distance to the left
        # reverse the trees_left list to start from the current tree
        trees_left = trees_left[::-1]
        for tree_left in trees_left:
            viewing_distance_left += 1
            if tree_left >= tree:
                break
        ## Count viewing distance to the right
        for tree_right in trees_right:
            viewing_distance_right += 1
            if tree_right >= tree:
                break
        
        # Go to the appropriate location in the columns
        column = columns[k]
        tree = column[j]
        
        # What trees are on either side of the current tree
        trees_up = column[:j]
        trees_down = column[j+1:]
        
        ## Count viewing distance up
        # reverse the trees_up list to start from the current tree
        trees_up = trees_up[::-1]
        for tree_up in trees_up:
            viewing_distance_up += 1
            if tree_up >= tree:
                break
        
        # Count viewing distance down
        for tree_down in trees_down:
            viewing_distance_down += 1
            if tree_down >= tree:
                break
        
        # calculate scenic score by multiplying viewing distances
        scenic_score = (viewing_distance_left *
                        viewing_distance_right *
                        viewing_distance_up *
                        viewing_distance_down)
        # append scenic score to a list
        scenic_scores.append(scenic_score)

print('The highest scenic value is ' + str(max(scenic_scores)))               