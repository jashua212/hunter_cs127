
# assignment 31

# import library for processing 2-dimensional csv files:
import pandas as pd

# import library for graphing data:
import matplotlib.pyplot as plt

# get user input:
outFile = input('Enter name of output file: ')
# for testing only - set user input (overwriting above):
outFile = 'internet_users_percentage.png'

# read the csv file (using pandas) and store in 'internet' variable:
internet = pd.read_csv('country_internet.csv')

# compute each country's percentage of internet users, and save it as
# a new column in 'internet':
internet['Percentage'] = (internet['Internet users']/internet['Population']) * 100


# use pandas's .idxmax method to get index of row with max 'Percentage' value:
rowIndex = internet['Percentage'].idxmax()

# use this 'rowIndex' to get the 'Country' name in that row:
country = internet['Country'][rowIndex]

# use this 'rowIndex' to also get the 'Percentage' value in that row:
percentage = internet['Percentage'][rowIndex]

# print country that has the max percentage of internet users,
# rounding percentage to 2 decimal places:
print('maximum percentage of all countries:', country, round(percentage, 2), '%')


# create a graph of 'Country' versus 'Percentage' (with labels):
internet.plot(x='Country', y='Percentage')

# save graph as an image file:
fig = plt.gcf()
fig.savefig(outFile)

# show the graph created above:
plt.show()
