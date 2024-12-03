"""
https://adventofcode.com/2022/day/7

Error: No space left on device
Perhaps you can delete some files to make space for the update?
The outermost directory is called /.
lines that begin with $ are commands you executed

cd x moves in one level
cd .. moves out one level
cd / switches the current directory to the outermost directory, /.

ls means list. It prints out all of the files and directories immediately 
contained by the current directory
123 abc means that the current directory contains a file named abc with size 123
dir xyz means that the current directory contains a directory named xyz

you need to determine the total size of each directory
the sum of the sizes of the files it contains, directly or indirectly.
"""

# Find all of the directories with a total size of at most 100000. 
# What is the sum of the total sizes of those directories?
import pandas as pd

# Make a dataframe with the home direcory already in it
directories_df = pd.DataFrame({'directory': ['/'], 'size': [0], 'files':['']})

# Make a list out of the data
with open('221207.txt') as file:
    commands = []
    for line in file:
        commands.append(line.strip())
        
# Make a list with all different directories in the data
# Append the different directories to the dataframe
directories = []
counter = 1
for i, command in enumerate(commands):
    if 'dir'in command:
        directory = command.split(' ')[1]
        # Check for similar named directories, if so change name with counter
        if directory in directories:
            counter = counter + 1
            directory_counter = directory + str(counter)
            
            commands[i] = 'dir ' + directory_counter
            
            directories.append(directory_counter)
            directories_df = directories_df.append({'directory': directory_counter,
                                                    'size': 0,
                                                    'files':[]},
                                                    ignore_index = True)
            
            # change next $ cd directory command as well
            for j, command in enumerate(commands[i:]):
                if command == '$ cd ' + directory:
                    commands[i+j] = '$ cd ' + directory_counter
                    break
        else:    
            directories.append(directory)
            directories_df = directories_df.append({'directory': directory,
                                                    'size': 0,
                                                    'files':[]},
                                                    ignore_index = True)
# Find all direct items in each directory
files = []
for i in directories_df.index:
    directory = directories_df['directory'][i]
    # Find command where this directory is accessed 
    try:
        command_number = commands.index('$ cd ' + directory)
        # +2 to skip $ cd and $ ls commands
        for command in commands[command_number+2:]:
            # When next $ cd command, stop adding files/directories
            if '$ cd ' in command:
                files = []
                break
            # Append files and directories to a list
            else:
                files.append(command)
                directories_df.at[i, 'files'] = files
    except:
        pass

# Calculate size of direct files in each dir
for i in directories_df.index:
    size  = 0
    files = directories_df['files'][i]
    for file in files:
        if file[0].isdigit():
            size = size + int(file.split(' ',)[0])
    directories_df.at[i, 'size'] = size

# Starting at the bottom, calculate size of each directory inside directories
reversed_directories_df = directories_df.iloc[::-1]
for i in reversed_directories_df.index:
    size = reversed_directories_df['size'][i]
    files = reversed_directories_df['files'][i]
    for file in files:
        if 'dir' in file:
            sub_dir = file.split(' ')[1]
            sub_dir_row = (
                reversed_directories_df.loc[reversed_directories_df['directory'] 
                                            == sub_dir])
            sub_dir_size = int(sub_dir_row['size'])
            size = size + sub_dir_size
            
            reversed_directories_df.at[i, 'size'] = size
        else:
            pass
        
# Make seperate df with all dir < 100000
directories_below_100000 = pd.DataFrame()    
for i in reversed_directories_df.index:
    size = int(reversed_directories_df['size'][i])
    if size <= 100000:
        directories_below_100000 = (
            directories_below_100000.append(
                reversed_directories_df.loc[i], ignore_index=True))
# Sum all sizes < 100000
sum_sizes = sum(directories_below_100000['size'])


### DOES NOT WORK YET!!!
# Total disk space available to the filesystem is 70000000
# To run the update, you need unused space of at least 30000000. 
# Find the smallest directory that, if deleted, would free up enough space on 
# the filesystem to run the update. What is the total size of that directory?

total_used_space = int(reversed_directories_df.loc[reversed_directories_df['directory'] 
                            == '/']['size'])
total_free_space = 70000000 - total_used_space
space_needed = 30000000 - total_free_space

# Order the dataframe by size:
ordered_df = reversed_directories_df.sort_values(by=['size'])

# Pick out the directories with size >= space needed
highest_df = pd.DataFrame()
for i in ordered_df.index:
    if ordered_df['size'][i] >= space_needed:
        highest_df = (
            highest_df.append(ordered_df.loc[i], ignore_index=True))

extra_space = highest_df['size'][0]

# answer should be: 9847279
