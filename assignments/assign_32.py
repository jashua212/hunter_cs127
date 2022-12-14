
# assignment 32

# import library for processing 2-dimensional csv files:
import pandas as pd

# import library for graphing data:
import matplotlib.pyplot as plt

# read the csv file (using pandas) and store in 'internet' variable:
internet = pd.read_csv('country_internet.csv')

# group the data into regions:
allRegionsData = internet.groupby('Continental region')

# print each region's mean number of internet plans:
column = 'NO. OF Internet Plans'    # store string in a variable
print(allRegionsData[column].mean())

# print various regions user can choose from:
print('\npossible regions are')
print(allRegionsData.groups.keys())

# get user's choice for a specific region:
choice = input('choose a region: ')
# for testing only - set user input (overwriting above):
choice = 'NORTHERN AMERICA'

# get sub-group data according to user's choice:
regionData = allRegionsData.get_group(choice)

# show statistics for this region:
print('In region', choice)
print('number of countries:', len(regionData['Country']))
print('maximum number of internet plans:', regionData[column].max())
print('minimum number of internet plans:', regionData[column].min())

# create a bar graph of all the countries in the region:
regionData.plot.bar(x='Country', y=column)

# adjust bar graph's size so its x-axis label will be fully visible:
plt.gcf().subplots_adjust(bottom=0.25)

# set bar graph's x-axis and y-axis labels:
plt.xlabel('Country in ' + choice)
plt.ylabel(column)

# get user input for name of output file:
outFile = input('Please enter output file name: ')
# for testing only - set user input (overwriting above):
outFile = 'internet_plans_northern_america.png'

# save bar graph as an image file:
plt.gcf().savefig(outFile)

# show the bar graph created above:
plt.show()
