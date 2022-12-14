
# assignment 27

# import library for processing 2-dimensional csv files:
import pandas as pd

# import library for graphing data:
import matplotlib.pyplot as plt

# get user inputs:
#inFile = input('Enter a csv file: ')
#boro = input('Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ')
#outFile = input('Enter output name: ')

# for testing only - set user inputs:
inFile = 'covid_daily_cases.csv'
boro = 'Queens'
outFile = 'queensCovidFraction.png'

# read the csv file (using pandas) and store in 'covid' variable:
covid = pd.read_csv(inFile)

# get the data for only the 'boro' chosen by user:
boroData = covid[boro]

# compute fraction of boro's daily cases, and save it as a new column in 'covid':
covid['Fraction'] = boroData/covid['case_count']

# create a graph of 'date_of_interest' versus 'Fraction' (with labels):
covid.plot(x='date_of_interest', y='Fraction')

# save graph as an image file:
fig = plt.gcf()
fig.savefig(outFile)

# show the graph created above:
plt.show()

# print out calculations performed on 'boroData':
print('Min:', boroData.min())
print('Max:', boroData.max())
print('Mean:', round(boroData.mean(), 3))
print('Median:', boroData.median())
print('Standard Deviation:', round(boroData.std(), 3))
