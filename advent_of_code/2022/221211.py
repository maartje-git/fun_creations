"""
https://adventofcode.com/2022/day/11

Monkeys are playing Keep Away with your missing things!
You realize the monkeys operate based on how worried you are about each item.

You take some notes (your puzzle input) on the items each monkey currently has, 
how worried you are about those items, 
and how the monkey makes decisions based on your worry level.

data:
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Starting items lists your worry level for each item
Operation shows how your worry level changes as that monkey inspects an item
Test shows how the monkey uses your worry level to decide where to throw an 
item next.

After each monkey inspects an item but before it tests your worry level, your 
relief that the monkey's inspection didn't damage the item causes your worry 
level to be divided by three and rounded down to the nearest integer.

On a single monkey's turn, it inspects and throws all of the items it is 
holding one at a time and in the order listed. = A ROUND

When a monkey throws an item to another monkey, the item goes on the end of the 
recipient monkey's list. A monkey that starts a round with no items could end 
up inspecting and throwing many items by the time its turn comes around. If a 
monkey is holding no items at the start of its turn, its turn ends.

Count the total number of times each monkey inspects items over 20 rounds
"""


import pandas as pd
import math


number_of_rounds = 10000

# Read the file and make a list of all lines
data = []
with open('221211.txt') as file:
    for line in file:
        data.append(line.strip())

#%% Part 1 The level of monkey business in can be found by multiplying these 
# together for the two most active monkeys

# Get all the info per monkey and append to dictionary
monkeys = {}
for i in range(round(len(data)/7)):
    monkey = data[i*7].replace(':', '')
    items = data[i*7+1].replace('Starting items: ', '').split(', ',)
    operation_sign = data[i*7+2].replace('Operation: ', '').split(' ',)[3]
    operation_number = data[i*7+2].replace('Operation: ', '').split(' ',)[4]
    test = data[i*7+3].replace('Test: divisible by ', '')
    if_true = data[i*7+4].replace('If true: throw to monkey ', 'Monkey ')
    if_false = data[i*7+5].replace('If false: throw to monkey ', 'Monkey ')
    inspected_items = 0

    monkeys[monkey] = (items, 
                       operation_sign, 
                       operation_number, 
                       test, 
                       if_true, 
                       if_false,
                       inspected_items)

# make a dataframe from the monkey info
df = pd.DataFrame.from_dict(monkeys, 
                       orient='index', 
                       columns=['items', 
                                'operation_sign', 
                                'operation_number',
                                'devision_test',
                                'if_true',
                                'if_false',
                                'inspected_items'])

# loop through the monkeys and inspect, calculate, throw items
for i in range(number_of_rounds):
    for monkey in df.index:
        items = df['items'][monkey]
        operation_sign = df['operation_sign'][monkey]
        operation_number = df['operation_number'][monkey]
        devision_test = int(df['devision_test'][monkey])
        if_true = df['if_true'][monkey]
        if_false =df['if_false'][monkey]
        
        # Keep track of inspected items per monkey
        items_inspected = df['inspected_items'][monkey]
        df['inspected_items'][monkey] = items_inspected + len(items)
        
        # For every item the monkey holds loop through all actions
        for i in range(len(items)):
            item = items[i]
            if operation_number == 'old':
                current_operation_number = item
            else:
                current_operation_number = operation_number
            # How much does your worry level changes as that monkey inspects
            new_item = eval(item + operation_sign + current_operation_number)

            # Relief devides worry level by three and rounded down
            new_item = math.floor(new_item / 3)

            # test to decide where to throw an item next
            if new_item%devision_test == 0:
                new_monkey = if_true
            else:
                new_monkey = if_false
            
            #throw items to the appropriate monkey
            items_new_monkey = df['items'][new_monkey]
            items_new_monkey.append(str(new_item))
            df['items'][new_monkey] = items_new_monkey
        
        # empty the list of the current monkey 
        df['items'][monkey] = []

# Calculate the level of monkey business by multiplying together the most 
# active monkeys inspected items
monkey_business = (df['inspected_items'].nlargest(2)[0] * 
                   df['inspected_items'].nlargest(2)[1])

#%% part 2 Worry levels are no longer divided by three after each item is 
# inspected. Starting again from the initial state in your puzzle input, 
# what is the level of monkey business after 10000 rounds?

# Get all the info per monkey and append to dictionary
monkeys = {}

for i in range(round(len(data)/7)):
    monkey = data[i*7].replace(':', '')
    items = data[i*7+1].replace('Starting items: ', '').split(', ',)
    operation_sign = data[i*7+2].replace('Operation: ', '').split(' ',)[3]
    operation_number = data[i*7+2].replace('Operation: ', '').split(' ',)[4]
    test = data[i*7+3].replace('Test: divisible by ', '')
    if_true = data[i*7+4].replace('If true: throw to monkey ', 'Monkey ')
    if_false = data[i*7+5].replace('If false: throw to monkey ', 'Monkey ')
    inspected_items = 0

    monkeys[monkey] = (items, 
                       operation_sign, 
                       operation_number, 
                       test, 
                       if_true, 
                       if_false,
                       inspected_items)

# make a dataframe from the monkey info
df = pd.DataFrame.from_dict(monkeys, 
                       orient='index', 
                       columns=['items', 
                                'operation_sign', 
                                'operation_number',
                                'devision_test',
                                'if_true',
                                'if_false',
                                'inspected_items'])

# calculate the Least Common Multiple op devision_tests for relief
devision_tests = []
for monkey in df.index:
    devision_tests.append(int(df['devision_test'][monkey]))
lcm = math.lcm(*devision_tests)

# loop through the monkeys and inspect, calculate, throw items
for i in range(number_of_rounds):
    for monkey in df.index:
        items = df['items'][monkey]
        operation_sign = df['operation_sign'][monkey]
        operation_number = df['operation_number'][monkey]
        devision_test = int(df['devision_test'][monkey])
        if_true = df['if_true'][monkey]
        if_false =df['if_false'][monkey]
        
        
        # Keep track of inspected items per monkey
        items_inspected = df['inspected_items'][monkey]
        df['inspected_items'][monkey] = items_inspected + len(items)
        
        # For every item the monkey holds loop through all actions
        for i in range(len(items)):
            item = items[i]
            if operation_number == 'old':
                current_operation_number = item
            else:
                current_operation_number = operation_number
            # How much does your worry level changes as that monkey inspects
            new_item = eval(item + operation_sign + current_operation_number)

            # Relief by Least Common Multiple
            new_item = new_item % lcm

            # test to decide where to throw an item next
            if new_item%devision_test == 0:
                new_monkey = if_true
            else:
                new_monkey = if_false
            
            #throw items to the appropriate monkey
            items_new_monkey = df['items'][new_monkey]
            items_new_monkey.append(str(new_item))
            df['items'][new_monkey] = items_new_monkey
        
        # empty the list of the current monkey 
        df['items'][monkey] = []

# Calculate the level of monkey business by multiplying together the most 
# active monkeys inspected items
monkey_business = (df['inspected_items'].nlargest(2)[0] * 
                   df['inspected_items'].nlargest(2)[1])
print(monkey_business)