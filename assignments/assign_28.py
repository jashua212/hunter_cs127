
# assignment 28

# import library for processing 2-dimensional csv files:
import pandas as pd

# read the csv file (using pandas) and store in 'lead' variable:
lead = pd.read_csv('children_lead.csv')

# get user's choice for grouping:
groupChoice = input('''Enter a choice:
a. group by borough
b. group by year
''')

# group data according to user's choice for grouping:
if groupChoice == 'a':
    print('average number of affected children by borough')
    groupData = lead.groupby('borough')
    print(groupData['affected_children'].mean())

    # get user's choice for specific borough:
    subChoice = input('Enter a borough: ')

    # set preposition to use in message to user:
    prep = 'of '

elif groupChoice == 'b':
    print('average number of affected children by year')
    groupData = lead.groupby('year')
    print(groupData['affected_children'].mean())

    # get user's choice for specific year - 'year' MUST BE converted to an
    # integer b/c pandas treats all numbers as integers, instead of strings:
    subChoice = int(input('Enter a year (2005 - 2016): '))

    # set preposition to use in message to user:
    prep = 'in '

else:
    print('wrong choice')
    quit() # exit immediately

# get sub-group data from groupData and show its statistics
subGroupData = groupData.get_group(subChoice)['affected_children']
msg = 'number of affected children ' + prep + str(subChoice) + ' is'
print('average', msg, subGroupData.mean())
print('min', msg, subGroupData.min())
print('max', msg, subGroupData.max())
